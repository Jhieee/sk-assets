import os
import sys
import unicodedata
from PIL import Image

# Force UTF-8 encoding for Windows terminal stdout to avoid encoding errors
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEROES_DIR = os.path.join(BASE_DIR, "heroes")

def main():
    if not os.path.exists(HEROES_DIR):
        print(f"Error: Heroes directory '{HEROES_DIR}' does not exist.")
        sys.exit(1)
        
    print("Scanning heroes directory for JPG files...")
    jpg_files = [f for f in os.listdir(HEROES_DIR) if f.lower().endswith(".jpg")]
    print(f"Found {len(jpg_files)} JPG files.")
    
    converted_count = 0
    for f in jpg_files:
        src_path = os.path.join(HEROES_DIR, f)
        
        # Normalize Korean filename to NFC (precomposed) to handle macOS NFD spelling issues
        norm_name = unicodedata.normalize('NFC', f)
        name_without_ext = os.path.splitext(norm_name)[0]
        dest_filename = f"{name_without_ext}.webp"
        dest_path = os.path.join(HEROES_DIR, dest_filename)
        
        try:
            with Image.open(src_path) as img:
                # Save directly as WebP with no scaling or cropping
                img.save(dest_path, "WEBP", quality=90)
            print(f"Converted: {f} -> {dest_filename}")
            converted_count += 1
        except Exception as e:
            print(f"Failed to convert {f}: {e}")
            
    print(f"\nSuccessfully converted {converted_count} files to WebP.")
    
    print("\nCleaning up original JPG files...")
    deleted_count = 0
    for f in os.listdir(HEROES_DIR):
        if f.lower().endswith(".jpg"):
            file_path = os.path.join(HEROES_DIR, f)
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete {f}: {e}")
                
    print(f"Deleted {deleted_count} JPG files.")
    print("Process completed.")

if __name__ == "__main__":
    main()
