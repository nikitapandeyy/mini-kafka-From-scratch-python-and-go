Good, the push worked. Two separate ideas are packed into that name.

## Git LFS

**Git LFS (Large File Storage)** is a Git extension for handling big files, like videos, datasets or model weights. Normal Git stores every version of every file forever, so large files make a repo huge and slow. With LFS, the big file lives on a separate server, and the repo only keeps a tiny pointer to it.

Your project is just text code, so you don't need it. Your repo had it enabled most likely because GitHub or the repo template set it up. It also isn't installed in Codespaces by default.

## Git hooks

A **hook** is a small script inside `.git/hooks/` that Git runs automatically when something happens: before a commit, after a commit, before a push, and so on. Hooks are how tools plug into Git without you doing anything.

## Putting them together

When LFS is enabled in a repo, it installs hooks like `pre-push` and `post-commit` that say "before pushing, upload any large files to the LFS server." But the hook needs the `git-lfs` program to do that. The program wasn't there, so the hook failed and Git cancelled your push.

That's why deleting the hook files fixed it. You removed the check that couldn't run, and since you have no large files, nothing was lost.

## If you ever need LFS later

You'd install `git-lfs` and run `git lfs install`. For example, if you store big benchmark datasets or model files in a future project, that's when it becomes useful. For this Kafka-like system, you can ignore it.

Ready for Module 1? We'll start with what a log, a partition and an offset are, so you can write the concepts section of the article.