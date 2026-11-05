B = {
    26: dict(e="The reading can't tell cDNA from everything else, so the number means nothing. ddPCR measures the specific cDNA instead.", nw="", hu=""),
    27: dict(e="Reagents run out and the enzyme tires, so the exponential phase ends. You can't work backward from the plateau.", nw="", hu=""),
    28: dict(e="A droplet with target amplifies to plateau and the dsDNA dye makes it bright; an empty droplet stays dim.", nw="", hu=""),
    29: dict(e="A droplet that started with one copy and one that started with three end up about equally bright at plateau, so brightness can't carry the count.", nw="", hu=""),
    30: dict(e="Average copies per droplet equals minus the natural log of the fraction negative. If there are no negatives, the math breaks.", nw="", hu=""),
    31: dict(e="With no negative droplets, Poisson can't tell 3 copies per droplet from 300. \"All blue\" is a failure, not a success.", nw="", hu=""),
    32: dict(e="It controls for differences in cell number, RNA input and RT efficiency, which raise all genes equally.", nw="", hu=""),
    33: dict(e="CNN is calponin, MHC is smooth muscle myosin heavy chain. Beta-actin may not stay steady in an actin experiment, so check your data.", nw="", hu=""),
    34: dict(e="If a housekeeping gene moves with treatment, normalizing to it adds error instead of removing it.", nw="", hu=""),
    35: dict(e="A longer product binds more dsDNA dye, so its positive droplets glow brighter. This is how you can tell mixed-up primer sets apart.", nw="", hu=""),
}
