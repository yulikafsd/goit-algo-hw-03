from pathlib import Path
import shutil
import sys


def copy_and_sort_dir(src_dir: Path, dst_dir: Path):

    # Iterate directory
    try:
        for el in src_dir.iterdir():

            # Case - directory: call copy_and_sort_dir recoursively
            if el.is_dir():
                copy_and_sort_dir(el, dst_dir)

            # Case - file:
            else:
                # Check file extension for sorting
                folder_name = el.suffix.lower().lstrip(".") or "no_extension"
                ext_folder = dst_dir / folder_name

                # Create new directory
                try:
                    ext_folder.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    print(f"Cannot create folder {ext_folder}: {e}")
                    continue

                # Copy file
                try:
                    shutil.copy2(el, ext_folder / el.name)
                    print(f"\nCopied {el.name}:\n{el} -> {ext_folder / el.name}")
                except Exception as e:
                    print(f"Cannot copy file {el}: {e}")

    except Exception as e:
        print(f"Cannot access directory {src_dir}: {e}")


def main():

    # Process command line args and create paths
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_dir> [destination_dir]")
        return

    src_path = Path(sys.argv[1]).resolve()
    dst_path = (
        Path(sys.argv[2]).resolve() if len(sys.argv) >= 3 else Path("dist").resolve()
    )

    # Abort if src directory does not exist
    if not src_path.exists() or not src_path.is_dir():
        print(f"Source directory does not exist: {src_path}")
        return

    # Create destination directory
    try:
        dst_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Cannot create destination directory {dst_path}: {e}")
        return

    # Call copy_and_sort_dir
    print(f"Copying files from {src_path} to {dst_path} ...")
    copy_and_sort_dir(src_path, dst_path)
    print("All files have been copied and sorted!")


if __name__ == "__main__":
    main()
