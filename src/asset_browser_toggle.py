import bpy
from bpy.types import Operator


class ASSET_OT_browser_toggle(Operator):
    """Toggle Asset Browser area in current workspace"""
    bl_idname = "asset.browser_toggle"
    bl_label = "Toggle Asset Browser"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        screen = context.screen
        
        asset_browser_area = None
        for area in screen.areas:
            if area.type == 'FILE_BROWSER':
                for space in area.spaces:
                    if space.type == 'FILE_BROWSER' and hasattr(space, 'browse_mode') and space.browse_mode == 'ASSETS':
                        asset_browser_area = area
                        break
                if asset_browser_area:
                    break
        
        if asset_browser_area:
            self.remove_asset_browser(context, asset_browser_area)
            self.report({'INFO'}, "Asset Browser closed")
        else:
            self.add_asset_browser(context)
            self.report({'INFO'}, "Asset Browser opened")
        
        return {'FINISHED'}
    
    def add_asset_browser(self, context):
        screen = context.screen
        
        # Find the leftmost visible area (not hidden/minimized)
        visible_areas = [area for area in screen.areas if area.width > 100 and area.height > 100]
        if not visible_areas:
            self.report({'ERROR'}, "No visible areas found")
            return
            
        first_area = min(visible_areas, key=lambda area: area.x)
        
        region = None
        for reg in first_area.regions:
            if reg.type == 'WINDOW':
                region = reg
                break
        
        if not region:
            self.report({'ERROR'}, "Could not find valid region to split")
            return
        
        override_context = {
            'area': first_area,
            'region': region,
            'screen': screen,
            'window': context.window
        }
        
        with context.temp_override(**override_context):
            bpy.ops.screen.area_split(direction='HORIZONTAL', factor=0.3)
        
        topmost_area = min(screen.areas, key=lambda area: area.y)
        topmost_area.type = 'FILE_BROWSER'
        
        for space in topmost_area.spaces:
            if space.type == 'FILE_BROWSER':
                space.browse_mode = 'ASSETS'
                break
    
    def remove_asset_browser(self, context, asset_browser_area):
        screen = context.screen
        
        # Check if this area can be safely closed (there should be at least 2 areas)
        if len(screen.areas) <= 1:
            self.report({'ERROR'}, "Cannot close the only remaining area")
            return
        
        region = None
        for reg in asset_browser_area.regions:
            if reg.type == 'WINDOW':
                region = reg
                break
        
        if not region:
            self.report({'ERROR'}, "Could not find valid region")
            return
        
        override_context = {
            'area': asset_browser_area,
            'region': region,
            'screen': screen,
            'window': context.window
        }
        
        try:
            with context.temp_override(**override_context):
                bpy.ops.screen.area_close()
        except Exception as e:
            self.report({'ERROR'}, f"Failed to close area: {str(e)}")
            return


def register_keymap():
    """Register keyboard shortcut for asset browser toggle"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Screen', space_type='EMPTY')
        km.keymap_items.new(ASSET_OT_browser_toggle.bl_idname, 'SPACE', 'PRESS', alt=True)


def unregister_keymap():
    """Unregister keyboard shortcut for asset browser toggle"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.get('Screen')
        if km:
            for kmi in km.keymap_items:
                if kmi.idname == ASSET_OT_browser_toggle.bl_idname:
                    km.keymap_items.remove(kmi)
                    break


def register():
    bpy.utils.register_class(ASSET_OT_browser_toggle)
    register_keymap()


def unregister():
    unregister_keymap()
    bpy.utils.unregister_class(ASSET_OT_browser_toggle)


if __name__ == "__main__":
    register()