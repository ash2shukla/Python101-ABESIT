import zlib
import tarfile
import zipfile
import os
import glob


def compress_string():
    s = b'witch which has which witches wrist watch'
    t = zlib.compress(s)
    print(len(s), len(t))


def bundle_without_compression(filepaths, tarname):
    tf = tarfile.open(tarname, "w")
    for _file in filepaths:
        tf.add(_file)
    tf.close()


def compress_to_zip(filepaths, zipname):
    zf = zipfile.ZipFile(zipname, 'w')
    for _file in filepaths:
        zf.write(_file)
    zf.close()


if __name__ == "__main__":
    compress_string()
    os.chdir('/home/troll/Python101-ABESIT/Syllabus')
    files = glob.glob('*')
    abs_paths = [os.path.abspath(i) for i in files]
    bundle_without_compression(abs_paths, 'mytar')
    compress_to_zip(abs_paths, 'myzip')