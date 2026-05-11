import os

def extract_bytes(file_path):
    try:
        file_path = file_path.strip().strip('"').strip("'")

        with open(file_path, 'rb') as f:
            byte_data = f.read()

        hex_bytes = [f'0x{byte:02x}' for byte in byte_data]

        cpp_array_name = (
            os.path.splitext(os.path.basename(file_path))[0]
            .replace('.', '_')
            .replace('-', '_')
            + "_bytes"
        )

        cpp_output = (
            f"unsigned char {cpp_array_name}[] = {{\n    "
            + ", ".join(hex_bytes)
            + "\n}};"
        )

        out_file = os.path.join(os.path.dirname(file_path), "bytes.txt")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(cpp_output)

        return f"Saved to {out_file}"

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    file_path = input("Please enter the path to your file: ")
    print(extract_bytes(file_path))
