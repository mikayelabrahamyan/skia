import os
import tarfile

def add_directory_to_tar(tar, directory, arc_directory):
    """Recursively adds a directory to the tar file."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            arc_path = os.path.join(arc_directory, os.path.relpath(full_path, start=directory))
            tar.add(full_path, arcname=arc_path)

def main():
    # Base path to the project directory
    base_path = os.path.dirname(os.path.abspath(__file__))

    directories = ["src", "modules", "include"]

    lib_src_path = os.path.join(base_path, "out", "canvaskit_wasm")

    filename = "output.tar.gz"
    archive_path = os.path.join(base_path, filename)

    with tarfile.open(archive_path, "w:gz") as tar:
        # Add directories to the tar.gz file
        for directory in directories:
            full_directory_path = os.path.join(base_path, directory)
            add_directory_to_tar(tar, full_directory_path, directory)

        # Add .a files from out/canvaskit_wasm to the tar.gz file under 'lib'
        lib_arc_directory = "lib"
        for file in os.listdir(lib_src_path):
            if file.endswith(".a"):
                full_path = os.path.join(lib_src_path, file)
                arc_path = os.path.join(lib_arc_directory, file)
                tar.add(full_path, arcname=arc_path)

    print("Archive created successfully at:", archive_path)

if __name__ == "__main__":
    main()