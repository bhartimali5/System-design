from abc import ABC, abstractmethod
import os


# ─── Strategy Interface ───────────────────────────────────────
class FileCompressorStrategy(ABC):
    @abstractmethod
    def compress(self, filename: str) -> str:
        pass

    @abstractmethod
    def decompress(self, filename: str) -> str:
        pass


# ─── Concrete Strategies ──────────────────────────────────────
class ZipStrategy(FileCompressorStrategy):
    def compress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]    # "document"
        compressed = f"{name}.zip"              # "document.zip"
        print(f"Compressing {filename} using ZIP algorithm")
        print(f"{filename} → {compressed} ")
        return compressed                        

    def decompress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]    # "document"
        decompressed = f"{name}.txt"            # "document.txt"
        print(f"Decompressing {filename} using ZIP algorithm")
        print(f"{filename} → {decompressed} ")
        return decompressed


class RarStrategy(FileCompressorStrategy):
    def compress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]
        compressed = f"{name}.rar"
        print(f"Compressing {filename} using RAR algorithm")
        print(f"{filename} → {compressed} ")
        return compressed

    def decompress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]
        decompressed = f"{name}.txt"
        print(f"Decompressing {filename} using RAR algorithm")
        print(f"{filename} → {decompressed} ")
        return decompressed


class GzipStrategy(FileCompressorStrategy):
    def compress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]
        compressed = f"{name}.gz"
        print(f"Compressing {filename} using GZIP algorithm")
        print(f"{filename} → {compressed} ")
        return compressed

    def decompress(self, filename: str) -> str:
        name = os.path.splitext(filename)[0]
        decompressed = f"{name}.txt"
        print(f"Decompressing {filename} using GZIP algorithm")
        print(f"{filename} → {decompressed} ")
        return decompressed


# ─── Context ──────────────────────────────────────────────────
class FileCompressor:
    def __init__(self, strategy: FileCompressorStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: FileCompressorStrategy) -> None:
        self._strategy = strategy
        print(f"Strategy switched to {strategy.__class__.__name__}")

    def compress(self, filename: str) -> str:
        return self._strategy.compress(filename)

    def decompress(self, filename: str) -> str:
        return self._strategy.decompress(filename)


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":

    compressor = FileCompressor(ZipStrategy())

    # Compress
    compressed_file = compressor.compress("document.txt")

    # Decompress — use returned filename 
    compressor.decompress(compressed_file)

    # Swap to GZIP 
    print()
    compressor.set_strategy(GzipStrategy())
    compressor.compress("document.txt")

    # Swap to RAR 
    print()
    compressor.set_strategy(RarStrategy())
    compressor.compress("report.pdf")
