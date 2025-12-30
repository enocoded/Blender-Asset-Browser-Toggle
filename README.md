# Blender Asset Browser Toggle

A Blender addon that provides a convenient keyboard shortcut to toggle the Asset Browser area in your workspace.

## Features

- **Quick Toggle**: Press `Alt+Space` to instantly show/hide the Asset Browser
- **Smart Area Management**: Automatically splits the first visible area horizontally when opening
- **Clean Removal**: Uses proper area closing when hiding the Asset Browser
- **Hidden Panel Safe**: Correctly handles hidden/minimized panels by filtering for visible areas only
- **No UI Conflicts**: Avoids cursor issues and stuck join arrows

## Installation

### Method 1: Script Directories (Recommended)
1. Download or clone this repository to your desired location (e.g., `C:\Scripts\Blender-Asset-Browser-Toggle\`)
2. Open Blender and go to `Edit` → `Preferences` → `File Paths`
3. In the **Scripts** section, click the folder icon and add the path to your project root directory
   ```
   Example: C:\GitHub\Blender-Asset-Browser-Toggle\
   ```
4. Click "Save Preferences" and restart Blender
5. Go to `Edit` → `Preferences` → `Add-ons`
6. Search for "Asset Browser Toggle" in the Interface category
7. Enable the addon by checking the checkbox
8. The shortcut will be automatically available

### Method 2: Manual Install
1. Download the `asset_browser_toggle` folder from `addons/asset_browser_toggle/`
2. Copy it to your Blender addons directory:
   ```
   Windows: %APPDATA%\Blender Foundation\Blender\4.4\scripts\addons\
   macOS: ~/Library/Application Support/Blender/4.4/scripts/addons/
   Linux: ~/.config/blender/4.4/scripts/addons/
   ```
3. Restart Blender
4. Go to `Edit` → `Preferences` → `Add-ons`
5. Search for "Asset Browser Toggle" and enable it

### Important: Shortcut Conflict
⚠️ **Note**: The default shortcut conflicts with Blender's built-in "Toggle Maximize Area" command. You'll need to remove or change the default shortcut first:

1. Go to `Edit` → `Preferences` → `Keymap`
2. Search for "Toggle Maximize Area" 
3. Either delete the existing binding or change it to a different key combination
4. Save preferences

## Usage

- **Open Asset Browser**: Press the hotkey when no Asset Browser is visible
  - Splits the leftmost visible area horizontally (30% for Asset Browser)
  - Automatically sets the new area to Asset Browser mode
  
- **Close Asset Browser**: Press the hotkey when Asset Browser is visible
  - Cleanly removes the Asset Browser area
  - Restores the original layout

## Technical Details

### How It Works
- Detects existing Asset Browser areas by checking for `FILE_BROWSER` type with `ASSETS` browse mode
- When opening: finds the leftmost visible area (width/height > 100px) and splits it horizontally
- When closing: uses `bpy.ops.screen.area_close()` for clean area removal
- Uses proper context override for reliable operator execution

### File Structure
```
Blender-Asset-Browser-Toggle/
├── addons/
│   └── asset_browser_toggle/
│       └── __init__.py
└── README.md
```

### Compatibility
- **Blender Version**: 4.4+ (uses modern `temp_override` context system)
- **Workspace**: Works in any workspace layout
- **Areas**: Compatible with all area types (3D Viewport, Shader Editor, etc.)

## Troubleshooting

### Common Issues

**Q: Addon doesn't appear in preferences**
- A: Make sure you added the project root directory (not the addons subfolder) in Script Directories
- A: Verify the file structure matches the layout above
- A: Check System Console for Python errors during startup
- A: Restart Blender after adding the script directory path

**Q: Hotkey doesn't work after enabling addon**
- A: **Most common issue**: Remove Blender's default "Toggle Maximize Area" shortcut first (see Installation section)
- A: Check if the shortcut conflicts with other system hotkeys
- A: Verify the addon is enabled with a checkmark in Add-ons preferences

**Q: Script not loading automatically**
- A: Ensure you added the correct directory path in `Edit` → `Preferences` → `File Paths` → `Scripts`
- A: The path should point to the project root, not the addons subfolder
- A: Restart Blender after adding the script directory path

**Q: Split happens in wrong area**
- A: The script targets the leftmost visible area - hide areas you don't want split

### Debug Information
Check if the addon is registered by running this in Blender's Python Console:
```python
import bpy
print(hasattr(bpy.ops.asset, 'browser_toggle'))
```

## Future Updates

- **Enhanced UI Integration**: Additional workspace integration options
- **Customizable Split Ratio**: User-configurable split percentage
- **Multiple Browser Support**: Handle multiple asset browser instances

## Contributing

Feel free to submit issues, feature requests, or pull requests. This addon was designed to be simple and reliable for everyday Blender workflow enhancement.

## License

This project is released under the MIT License - feel free to modify and distribute as needed.

## Changelog

### v1.2 (latest)
- **Converted to Proper Addon**: Added `bl_info` and proper addon structure
- **Improved Installation**: Added Script Directories method with addon management
- **Enhanced File Structure**: Organized as standard Blender addon with `__init__.py`
- **Refactored Shortcut Registration**: Improved hotkey registration and unregistration process
- **Updated Author**: Changed author to "enocoded"

### v1.1
- **Improved Area Safety**: Added check to prevent closing the only remaining area
- **Enhanced Error Handling**: Better exception handling for area close operations
- **Refined Area Detection**: Improved logic for finding and managing asset browser areas
- **Code Cleanup**: Streamlined area splitting and detection methods
- **Bug Fixes**: Resolved issues with area visibility and positioning edge cases

### v1.0
- Initial release with basic toggle functionality
- Added keyboard shortcut registration
- Implemented proper area management
- Fixed hidden panel detection issues
