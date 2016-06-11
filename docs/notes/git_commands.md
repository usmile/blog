# 第一章 入门介绍

> git 命令 [commands](./res/github-git-cheat-sheet.pdf)

## 1.1 基本命令
```bash
mkdir notes
cd notes

# 初始化一个git仓库 
git init

echo "my notes" > readme.md

# 查看状态
git status
# 查看修改内容
git diff readme.md

# 添加文件到仓库
git add readme.md
# 提交更改
git commit -m "add readme"

# 查看提交日志
git log --pretty=oneline

# 回退到上一个版本
git reset --hard HEAD^
HEAD: 当前版本
HEAD^: 上一个版本
HEAD~100: 前一百个版本
58a65b: 指定版本

# 查看命令历史
git reflogs
```

## 1.2 工作区
工作区 -add-> 暂存区 -commit-> 分支

```bash
# 查看工作区与暂存区文件的差异
git diff readme.md

# 查看工作区和版本库最新版本的差异
git diff HEAD -- readme.md

# 放弃工作区的修改
git checkout -- readme.md

# 撤销暂存区
git reset HEAD readme.md
```

# 第二章 远程仓库
## 2.1 创建一个库推送到github
在github上创建一个仓库 gitlearn

在本地创建一个gitlearn目录，并进入

    mkdir gitlearn
    cd gitlearn

使用命令git init初始化一个库

    git init

然后使用如下命令添加远程库 origin

    git remote add origin git@github.com:usmile/gitlearn.git

生成一个readme.md文件

    echo "git learn is very easy!" > readme.md

添加文件到仓库

    git add readme.md

提交更改

    git commit -m "add readme file"

执行向远程仓库origin master分支推送更新

    git push -u origin master    


## 2.2 克隆一个远程仓库

在github上创建一个仓库 gitlearn

从github上克隆仓库

    git clone git@github.com:usmile/gitlearn.git




# 第三章 分支管理
## 3.1 创建于合并分支
```bash
# 创建分支
git branch dev
# 切换分支
git checkout dev

# 创建并切换分支
git checkout -b dev

# 查看分支, 带有*的分支为当前分支
git branch

# 切换到master分支
git checkout master
# 合并指定分支到当前分支
git merge dev 

# 删除分支
git branch -d dev
```

## 3.2 冲突管理

在master分支上修改readme.md，新增一行内容。提交修改。
在dev分支上修改readme.md，也新增一行内容。提交修改。

然后切换到master分支，将dev分支的内容合并。

    git merge dev

会有冲突提醒。打开 readme.md:

```bash
 <<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.
>>>>>>> feature1
```

然后修改内容。再次提交。


```bash
# 查看分支合并情况
git log --graph  --pretty=oneline --abbrev-commit
```

```bash
# 工作现场“储藏”
git stash

# 查看储藏的你内容
git stash list

# 恢复储藏的内容
git stash apply stash@{0}

# 删除储藏的内容
git stash drop

# 恢复储藏的内容，并删除
git stash pop
```


# 第四章 搭建服务

```bash
(server)
# 创建一个用户git来运行git服务
adduser git

# 创建一个裸仓库(sample.git 所在目录/root/git/)
git init --bare sample.git

# 改变用户
sudo chown -R git:git sample.git

# 添加客户端的公钥到/root/.ssh/authorized_keys

(client)
# 克隆sample.git
git clone git@192.168.137.200:/root/git/sample.git

# 增加readme.md
echo "my first server sample" > readme.md
git add readme.md
git command "my first server sample"
git push
```
