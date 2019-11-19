from Mid_max_IV import reduction
I=[93,95,96,97,98]
varpoly=[[[93,95,1],[93,96,3],[97,98,4],[97,98,4,287],[95,96,286],[1,3,287]],[[96,3],[95,96]]]
u1,u2=reduction(I,varpoly).Mid_monoment_main()
print(u1)
print(u2)