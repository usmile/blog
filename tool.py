# -*-coding: utf-8
from glob import glob
from os import chdir

# generate mkdocs.yml

mkdocs = '''\
# 这个文件由 tool.py 自动生成，不要手动修改
site_name: 博客 
site_dir: ../usmile.github.com/
theme: bootstrap
docs_dir: docs
markdown_extensions: [toc, tables]
'''

pages = ""

def gen_pages():

    global pages

    fmt = "- [%32s, %16s]"

    pages = "pages: \n  " + fmt + "\n"

    pages = pages % ("index.md", "首页")

    dirs = {
        r"./articles/":    "文章",
        r"./notes/":       "笔记",
        r"./translate/":   "翻译",
        r"./life/":        "生活"
    } 

    pages_fmt = "  " + fmt + "\n"

    for path in sorted(dirs):
        for md in glob(path + "/*.md"):
            md = md.replace("\\", "/")
            if path in md:
                pages = pages + pages_fmt % (md, dirs[path])

    pages = pages + "  " + fmt + "\n" 
    pages = pages % ("about.md", "关于")



def main():
    global mkdocs
    global pages 

    chdir("./docs/")
    gen_pages()
    chdir("../")

    mkdocs = mkdocs + pages
    import codecs
    with codecs.open("./mkdocs.yml", "w", "utf-8") as mkdocs_yml:
        mkdocs_yml.write(mkdocs)

if __name__ == '__main__':
    main() 
