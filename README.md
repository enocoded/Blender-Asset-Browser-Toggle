# Blender Asset Browser Toggle

A Blender Python script that provides a convenient keyboard shortcut to toggle the Asset Browser area in your workspace.

## Features

- **Quick Toggle**: Press `Alt+Space` to instantly show/hide the Asset Browser
- **Smart Area Management**: Automatically splits the first visible area horizontally when opening
- **Clean Removal**: Uses proper area closing when hiding the Asset Browser
- **Hidden Panel Safe**: Correctly handles hidden/minimized panels by filtering for visible areas only
- **No UI Conflicts**: Avoids cursor issues and stuck join arrows

## Installation

### Auto-Load on Startup (Recommended)
1. Copy `asset_browser_toggle.py` to your Blender startup scripts folder:
   ```
   Windows: %APPDATA%\Blender Foundation\Blender\4.4\scripts\startup\
   macOS: ~/Library/Application Support/Blender/4.4/scripts/startup/
   Linux: ~/.config/blender/4.4/scripts/startup/
   ```
2. Restart Blender - the script will automatically load and register the hotkey

### Important: Shortcut Conflict
⚠️ **Note**: The default shortcut conflicts with Blender's built-in "Toggle Maximize Area" command. You'll need to remove or change the default shortcut first:

1. Go to `Edit` → `Preferences` → `Keymap`
2. Search for "Toggle Maximize Area" 
3. Either delete the existing binding or change it to a different key combination
4. Save preferences and restart Blender

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

### Compatibility
- **Blender Version**: 4.4+ (uses modern `temp_override` context system)
- **Workspace**: Works in any workspace layout
- **Areas**: Compatible with all area types (3D Viewport, Shader Editor, etc.)

## Troubleshooting

### Common Issues

**Q: Hotkey doesn't work**
- A: Make sure the script is in the startup folder and Blender has been restarted
- A: **Most common issue**: Remove Blender's default "Toggle Maximize Area" shortcut first (see Installation section)
- A: Check if the shortcut conflicts with other system hotkeys

**Q: Split happens in wrong area**
- A: The script targets the leftmost visible area - hide areas you don't want split

## Future Updates

- **Addon Version**: A proper Blender addon with UI integration is planned for future releases
- **Additional Features**: More customization options and workspace integration

## Contributing

Feel free to submit issues, feature requests, or pull requests. This script was designed to be simple and reliable for everyday Blender workflow enhancement.

## License

This project is released under the MIT License - feel free to modify and distribute as needed.

## Changelog

### v1.2 (latest)
- **Refactored Shortcut Registration**: Improved hotkey registration and unregistration process
- **Changed shortcut**: Updated default toggle to `Alt+Space` to avoid conflicts

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
