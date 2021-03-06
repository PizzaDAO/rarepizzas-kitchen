# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named testExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from testExt import *
except ImportError:
    pass

def getPluginID():
    return "test"

def getLabel():
    return "test"

def getVersion():
    return 1

def getGrouping():
    return "test"

def getPluginDescription():
    return "test plugin"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    del lastNode

    # Start of node "p4950"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("p4950")
    lastNode.setLabel("4950")
    lastNode.setPosition(994, 194)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupp4950 = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadPNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/topping/4950-topping-meat-turkeysausage.png")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("unpremult")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "p4950"

    # Start of node "p0000"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("p0000")
    lastNode.setLabel("0000")
    lastNode.setPosition(355, 186)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupp0000 = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadPNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/base/0000-base-box-cardboard.png")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("unpremult")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "p0000"

    # Start of node "p1000"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("p1000")
    lastNode.setLabel("1000")
    lastNode.setPosition(511, 194)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupp1000 = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadPNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/base/1000-base-crust-thin.png")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("unpremult")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "p1000"

    # Start of node "p3000"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("p3000")
    lastNode.setLabel("3000")
    lastNode.setPosition(829, 194)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupp3000 = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadPNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/base/3000-base-cheese-mozzarella.png")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("unpremult")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "p3000"

    # Start of node "p2000"
    lastNode = app.createNode("fr.inria.built-in.Read", 1, group)
    lastNode.setScriptName("p2000")
    lastNode.setLabel("2000")
    lastNode.setPosition(671, 186)
    lastNode.setSize(128, 78)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupp2000 = lastNode

    param = lastNode.getParam("decodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.ReadPNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/base/2000-base-sauce-tomato.png")
        del param

    param = lastNode.getParam("filePremult")
    if param is not None:
        param.set("unpremult")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "p2000"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(587, 359)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    del lastNode
    # End of node "Merge1"

    # Start of node "Transform1"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1")
    lastNode.setLabel("Transform1")
    lastNode.setPosition(841, 302)
    lastNode.setSize(104, 26)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform1 = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(0.9, 0)
        param.setValue(0.9, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform1"

    # Start of node "Transform2"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform2")
    lastNode.setLabel("Transform2")
    lastNode.setPosition(1006, 302)
    lastNode.setSize(104, 26)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform2 = lastNode

    param = lastNode.getParam("translate")
    if param is not None:
        param.setValue(1488, 0)
        param.setValue(956, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(392, 0)
        param.setValue(325.5, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform2"

    # Start of node "Write1"
    lastNode = app.createNode("fr.inria.built-in.Write", 1, group)
    lastNode.setScriptName("Write1")
    lastNode.setLabel("Write1")
    lastNode.setPosition(587, 483)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.75, 0.75, 0)
    groupWrite1 = lastNode

    param = lastNode.getParam("encodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.WritePNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/out/pizza.%.png")
        del param

    param = lastNode.getParam("formatType")
    if param is not None:
        param.set("input")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("HD")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Write1"

    groupgroup = groupWrite1
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = groupgroup
    lastNode.setColor(0.75, 0.75, 0)
    param = lastNode.getParam("encodingPluginID")
    if param is not None:
        param.setValue("fr.inria.openfx.WritePNG")
        del param

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/out/pizza.%.png")
        del param

    param = lastNode.getParam("formatType")
    if param is not None:
        param.set("input")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("HD")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, groupgroup)
    lastNode.setLabel("Output1")
    lastNode.setPosition(0, 0)
    lastNode.setSize(0, 0)
    lastNode.setColor(0, 0, 0)
    groupgroupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, groupgroup)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(0, 0)
    lastNode.setSize(0, 0)
    lastNode.setColor(0, 0, 0)
    groupgroupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "internalEncoderNode"
    lastNode = app.createNode("fr.inria.openfx.WritePNG", 1, groupgroup)
    lastNode.setScriptName("internalEncoderNode")
    lastNode.setLabel("internalEncoderNode")
    lastNode.setPosition(0, 0)
    lastNode.setSize(0, 0)
    lastNode.setColor(0, 0, 0)
    groupgroupinternalEncoderNode = lastNode

    param = lastNode.getParam("filename")
    if param is not None:
        param.setValue("/Users/anthonyshafer/Dropbox/RarePizzas/rarepizzas-shared/rarepizzas-ingredients-db/out/pizza.%.png")
        del param

    param = lastNode.getParam("formatType")
    if param is not None:
        param.set("input")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("HD")
        del param

    param = lastNode.getParam("ParamExistingInstance")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "internalEncoderNode"

    # Now that all nodes are created we can connect them together, restore expressions
    groupgroupOutput1.connectInput(0, groupgroupinternalEncoderNode)
    groupgroupinternalEncoderNode.connectInput(0, groupgroupSource)


    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("0000_Sync")
    lastNode.setPosition(828, 430)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Input2"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input2")
    lastNode.setLabel("1000_Sync")
    lastNode.setPosition(1019, 413)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput2 = lastNode

    del lastNode
    # End of node "Input2"

    # Start of node "Input3"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input3")
    lastNode.setLabel("2000_Sync")
    lastNode.setPosition(1305, 404)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput3 = lastNode

    del lastNode
    # End of node "Input3"

    # Start of node "Input4"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input4")
    lastNode.setLabel("3000_Sync")
    lastNode.setPosition(1658, 388)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput4 = lastNode

    del lastNode
    # End of node "Input4"

    # Start of node "Input5"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input5")
    lastNode.setLabel("4950_Sync")
    lastNode.setPosition(1987, 387)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput5 = lastNode

    del lastNode
    # End of node "Input5"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(587, 569)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupp4950.connectInput(0, groupInput5)
    groupp0000.connectInput(0, groupInput1)
    groupp1000.connectInput(0, groupInput2)
    groupp3000.connectInput(0, groupInput4)
    groupp2000.connectInput(0, groupInput3)
    groupMerge1.connectInput(0, groupp0000)
    groupMerge1.connectInput(1, groupp1000)
    groupMerge1.connectInput(3, groupp2000)
    groupMerge1.connectInput(4, groupTransform1)
    groupMerge1.connectInput(5, groupTransform2)
    groupTransform1.connectInput(0, groupp3000)
    groupTransform2.connectInput(0, groupp4950)
    groupWrite1.connectInput(0, groupMerge1)
    groupOutput1.connectInput(0, groupWrite1)

    try:
        extModule = sys.modules["testExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
