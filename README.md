# RV: Pixel Aspect Ratio Error

The *RV Player* of Autodesk's Flow Production Tracking (formerly know as ShotGrid) has a major issue when comparing Image Files.
When Image Sequences are compared with the replace tool, the pixel aspect ratio is forcefully set to 1, no matter the actual pixel aspect ratio, stretching or squishing the image.
**But only when the Image is shown in full.** Wiping resets the par to it's actual value making it impossible to compare files, since the second one is most likely not wiped.

> Details will follow here, until then you can find them here:\
> https://community.shotgridsoftware.com/t/rv-and-the-pixel-aspect-ratio/9787

Since the DevTeam of Autodesk has no idea on how to fix this yet, this little package makes possible to circumvent this.
To load it into RV, the content of the folder must be zipped into an RV Package (rvpkg) file. 
