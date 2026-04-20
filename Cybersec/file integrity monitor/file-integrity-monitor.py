
import hashlib
import argparse
from pathlib import Path


def get_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def read_baseline_hash(baseline_file):
    if not baseline_file.exists():
        return None
    return baseline_file.read_text(encoding="utf-8").strip()


def write_baseline_hash(baseline_file, hash_value):
    baseline_file.write_text(hash_value + "\n", encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple file integrity monitor")
    parser.add_argument(
        "file",
        nargs="?",
        default="file.txt",
        help="Path to the file to monitor (default: file.txt)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    file_path = Path(args.file).resolve()
    baseline_file = file_path.with_suffix(file_path.suffix + ".sha256")

    if not file_path.exists():
        print(f"[!] ERROR: File not found: {file_path}")
        raise SystemExit(1)

    current_hash = get_file_hash(file_path)
    stored_baseline_hash = read_baseline_hash(baseline_file)

    if stored_baseline_hash is None:
        write_baseline_hash(baseline_file, current_hash)
        print(f"[i] Baseline created at {baseline_file}")
        print(f"[i] Baseline Hash: {current_hash}")
    elif current_hash == stored_baseline_hash:
        print("[+] SUCCESS: File integrity verified. No changes detected.")
    else:
        print("[!] ALERT: Integrity compromised! File has been modified.")
        print(f"[i] Stored:  {stored_baseline_hash}")
        print(f"[i] Current: {current_hash}")


if __name__ == "__main__":
    main()
