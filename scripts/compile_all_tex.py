import pathlib
import subprocess
import os
from tqdm import tqdm

def find_tex_files(folder: pathlib.Path):
    return list(folder.rglob("*.tex"))

def delete_auxiliary_files(tex_path: pathlib.Path):
    extensions = [".aux", ".log", ".dvi", ".toc", ".out"]
    for ext in extensions:
        file = tex_path.with_suffix(ext)
        if file.exists():
            file.unlink()

def compile_tex(tex_path: pathlib.Path):
    tex_dir = tex_path.parent
    cwd_before = os.getcwd()
    os.chdir(tex_dir)
    log_path = tex_dir / f"{tex_path.stem}_compile.log"

    with log_path.open("w", encoding="utf-8") as f_log:
        try:
            subprocess.check_call(
                ["uplatex", "-interaction=nonstopmode", tex_path.name],
                stdout=f_log,
                stderr=subprocess.STDOUT
            )
            subprocess.check_call(
                ["dvipdfmx", tex_path.stem],
                stdout=f_log,
                stderr=subprocess.STDOUT
            )
        except subprocess.CalledProcessError:
            print(f"コンパイル失敗: {tex_path}")
        else:
            print(f"コンパイル成功: {tex_path}")
            delete_auxiliary_files(tex_path)
        finally:
            os.chdir(cwd_before)

def compile_all(folder_path: str):
    folder = pathlib.Path(folder_path)
    tex_files = find_tex_files(folder)
    if not tex_files:
        print("コンパイル対象の .tex が見つかりません。")
        return
    for tex_file in tqdm(tex_files):
        compile_tex(tex_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python compile_all_tex.py <folder_path>")
    else:
        compile_all(sys.argv[1])
