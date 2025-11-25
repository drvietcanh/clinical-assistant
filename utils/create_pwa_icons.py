"""
Create PWA Icons
Generates simple placeholder icons for PWA manifest
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def create_pwa_icon(size: int, output_path: Path):
    """
    Create a simple PWA icon with medical cross symbol
    
    Args:
        size: Icon size in pixels (e.g., 192, 512)
        output_path: Path to save the icon
    """
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle
    margin = size // 10
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        fill=(25, 118, 210, 255),  # Primary blue color
        outline=(25, 118, 210, 255)
    )
    
    # Medical cross (plus sign)
    cross_size = size // 3
    cross_thickness = size // 8
    center = size // 2
    
    # Horizontal line
    draw.rectangle(
        [center - cross_size // 2, center - cross_thickness // 2,
         center + cross_size // 2, center + cross_thickness // 2],
        fill=(255, 255, 255, 255)
    )
    
    # Vertical line
    draw.rectangle(
        [center - cross_thickness // 2, center - cross_size // 2,
         center + cross_thickness // 2, center + cross_size // 2],
        fill=(255, 255, 255, 255)
    )
    
    # Save icon
    img.save(output_path, 'PNG')
    print(f"✅ Created icon: {output_path} ({size}x{size})")


def main():
    """Create all required PWA icons"""
    static_dir = Path(__file__).parent.parent / "static"
    static_dir.mkdir(exist_ok=True)
    
    # Create icons
    sizes = [192, 512]
    for size in sizes:
        icon_path = static_dir / f"icon-{size}.png"
        create_pwa_icon(size, icon_path)
    
    print("\n✅ All PWA icons created successfully!")
    print(f"📁 Location: {static_dir}")
    print("\nNote: You can replace these with custom icons later.")


if __name__ == "__main__":
    try:
        from PIL import Image, ImageDraw
        main()
    except ImportError:
        print("❌ PIL/Pillow not installed. Installing...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image, ImageDraw
        main()

