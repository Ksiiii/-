#%%
# http1 = "https://s3.ananas.chaoxing.com/sv-w8/doc/70/07/e8/4e700d1d6651a1125343fed67092450e/thumb/"  # 导引
# for i in range(13):
#     print("![{}]("+http1+"{}.png)".format(i+1, i+1))

#%%
http2 = "https://s3.ananas.chaoxing.com/sv-w9/doc/b2/43/68/4176b09b1714eeaf112520a783817f72/thumb/"  # 分治
md = "分治.md"
with open(md, "w") as f:
    for i in range(13):
        f.write("![{}](" + http2 + "{}.png)".format(i + 1, i + 1))
#%%
Num = [13, 23, 32, 26, 33, 18]
Name = ["导引", "分治", "贪心", "动态规划", "回溯", "分支限界"]
Http = [
    "https://s3.ananas.chaoxing.com/sv-w8/doc/70/07/e8/4e700d1d6651a1125343fed67092450e/thumb/",
    "https://s3.ananas.chaoxing.com/sv-w9/doc/b2/43/68/4176b09b1714eeaf112520a783817f72/thumb/",
    "https://s3.ananas.chaoxing.com/sv-w7/doc/b7/29/27/fcb4c0a6b9cdfdf665dda3e72a9d7f83/thumb/",
    "https://s3.ananas.chaoxing.com/sv-w8/doc/a9/c2/ec/594e46e18d0c216c5bb93b85bceef316/thumb/",
    "https://s3.ananas.chaoxing.com/sv-w8/doc/f7/e9/f5/013d81aed49ec7fdb8e6c7977c7f3180/thumb/",
    "https://s3.ananas.chaoxing.com/sv-w9/doc/de/8d/7e/be61bf27ccb1b36a409b17ee22f19fd5/thumb/"
]
for i, num in enumerate(Num):
    md = "./1/"+Name[i]+".md"
    with open(md, "w") as f:
        for j in range(num):
            f.write("![{}](" + Http[i] + "{}.png)".format(j + 1, j + 1))
