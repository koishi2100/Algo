## info

此仓库用于存放个人 Algo.md 笔记并与他人共享，使用 git 共享协作。


## how to print

1. 合并 Algo.md 文档并解决冲突
2. 运行 `python split_md.py`，将文件切分成多个小文件，放在 released/raw/ 目录下
3. 使用 `Typora` 等编辑器将 released/raw/ 目录下的文件转换为 pdf 文件，放在 released/pdf/ 目录下，保留数学公式、代码高亮、md 语法等
4. 打开 WPS 手动为 released/pdf/*.pdf 文件添加插入目录
5. 运行 `python released/print_assmble.py`, 为 pdf 文件添加封面封底以及页码，导出到 released/print/ 目录下作为可打印的发行版本


## how to contribute

你怎么能直接 commit 到我的 main 分支啊？！GitHub 上不是这样！你应该先 fork 我的仓库，然后从 develop 分支 checkout 一个新的 feature 分支，比如叫 feature/confession。然后你把你的心意写成代码，并为它写好单元测试和集成测试，确保代码覆盖率达到95%以上。接着你要跑一下 Linter，通过所有的代码风格检查。然后你再 commit，commit message 要遵循 Conventional Commits 规范。之后你把这个分支 push 到你自己的远程仓库，然后给我提一个 Pull Request。在 PR 描述里，你要详细说明你的功能改动和实现思路，并且 @ 我和至少两个其他的评审。我们会 review 你的代码，可能会留下一些评论，你需要解决所有的 thread。等 CI/CD 流水线全部通过，并且拿到至少两个 LGTM 之后，我才会考虑把你的分支 squash and merge 到 develop 里，等待下一个版本发布。
你怎么直接上来就想 force push 到 main？！GitHub 上根本不是这样！我拒绝合并！