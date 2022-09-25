#imports
import bpy
from blenderbim.bim.ifc import IfcStore
import csv
file =IfcStore.get_file()

#####init the csv file###########
filename = "SturcturalElements.csv"
fields = ['objectType','T2','position','structure','material','dimensions','openings','connected From','Connected To']
row = []
#############     walls     ############################### 

FoundationW=[]    
for w in file.by_type('IfcWall'):
     if "Foundation" in w.ObjectType:
         FoundationW.append(w)
ExteriorW=[]
for w in file.by_type('IfcWall'):
     if "Exterior" in w.ObjectType:
         ExteriorW.append(w)
Party_walls=[]
for w in file.by_type('IfcWall'):
     if "Party" in w.ObjectType:
         Party_walls.append(w)
Walls=[FoundationW,ExteriorW,Party_walls]





#############################################################################################################
for wtype in Walls:
    if wtype ==FoundationW:
        wt="Foundation"
    if wtype ==ExteriorW:
        wt="Exterior Wall"
    if wtype ==Party_walls:
        wt="Party Wall"
        
    for w in wtype:
        wval=["Wall",wt]
        wval.append(w.ObjectPlacement)
        for relContainedInSpatialStructure in w.ContainedInStructure:
            #print(relContainedInSpatialStructure.RelatingStructure.Name)
            wval.append(relContainedInSpatialStructure.RelatingStructure.Name)
        for relAssociatesMaterial in w.HasAssociations:
            wval.append(relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers)
            #for M in relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers:
                #print(M.Material.Name)
                   
        ## get property sets attached to beams through IsDefinedBy"
        for definition in w.IsDefinedBy:    
            ## To support IFC2X3, we need to filter our results.
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                if property_set.Name == "PSet_Revit_Dimensions":
                    dval=[]
                    for property in property_set.HasProperties:
                        print(property.Name)
                        dval.append(property.NominalValue.wrappedValue)
                        print(property.NominalValue.wrappedValue)
                    wval.append(dval)
        oplist = []
        for openings in w.HasOpenings:
            oplist.append((openings.RelatedOpeningElement.Name,openings.RelatedOpeningElement.ObjectPlacement))
        wval.append(oplist)
        cflist = []
        for cf in w.ConnectedFrom:
            print("test")
            cflist.append(cf)
        wval.append(cflist)
        ctlist = []
        for ct in w.ConnectedTo:
            ctlist.append(ct)
        wval.append(ctlist)
        print(wval)
        row.append(wval)
        
#############     slabs     ##################################
Roof=[]
for s in file.by_type('IfcSlab'):
     if "Roof" in s.ObjectType:
         Roof.append(s)
FinishF=[]
for s in file.by_type('IfcSlab'):
     if "Finish" in s.ObjectType:
         FinishF.append(s)
ExteriorF=[]
for s in file.by_type('IfcSlab'):
     if "Exterior" in s.ObjectType:
         ExteriorF.append(s)
Slabs=[Roof,FinishF,ExteriorF]
for stype in Slabs:    #take only potentially loadbearing walls
    if stype ==FinishF:
        st= "Finish Floor"
    if stype ==ExteriorF:
        st="Exterior Floor"
    if stype ==Roof:
        st="Roof"
        
    for s in stype: #get all the walls properties
        sval=["Slab",st]
        print("#######################")
        sval.append(s.ObjectPlacement)
        for relContainedInSpatialStructure in s.ContainedInStructure:
            #print(relContainedInSpatialStructure.RelatingStructure.Name)
            sval.append(relContainedInSpatialStructure.RelatingStructure.Name)
        for relAssociatesMaterial in s.HasAssociations:
            sval.append(relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers)
            #for M in relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers:
                #print(M.Material.Name)
                   
        ## get property sets attached to beams through IsDefinedBy"
        for definition in s.IsDefinedBy:    
            ## To support IFC2X3, we need to filter our results.
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                if property_set.Name == "PSet_Revit_Dimensions":
                    dval=[]
                    for property in property_set.HasProperties:
                        dval.append(property.NominalValue.wrappedValue)
                    sval.append(dval)
        oplist = []
        for openings in s.HasOpenings:
            oplist.append((openings.RelatedOpeningElement.Name,openings.RelatedOpeningElement.ObjectPlacement))
        sval.append(oplist)
        sval.append([])
        sval.append([])
        #print(sval)  
        row.append(sval)


#############     beams     ##################################
Beams = file.by_type('IfcBeam')
btval= ["Beam",""]
for b in Beams:
    bval=["Beam",""]
    bval.append(b.ObjectPlacement)
    for relContainedInSpatialStructure in b.ContainedInStructure:
        #print(relContainedInSpatialStructure.RelatingStructure.Name)
        bval.append(relContainedInSpatialStructure.RelatingStructure.Name)
    for relAssociatesMaterial in b.HasAssociations:
        bval.append(relAssociatesMaterial.RelatingMaterial)
        #for M in relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers:
            #print(M.Material.Name)
                   
        ## get property sets attached to beams through IsDefinedBy"
    for definition in b.IsDefinedBy:    
            ## To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition

            if property_set.Name == "PSet_Revit_Dimensions":
                dval=[]
                for property in property_set.HasProperties:
                    dval.append(property.NominalValue.wrappedValue)
                bval.append(dval)
    bval.append([])#no openings
    bval.append([])#no connections 
    bval.append([])
    #print(bval)
    row.append(bval)

#########################  create the csv file   ############################################################
Filebrut=[fields,row]
with open(filename, 'w') as csvfile:
    # creating a csv writer object   
    # writing the fields5
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)4442