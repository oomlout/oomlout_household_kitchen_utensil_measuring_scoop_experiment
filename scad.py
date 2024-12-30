import copy
import opsc
import oobb
import oobb_base
import yaml
import os

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        navigation = False
        #navigation = True    

        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_household_kitchen_utensil_measuring_scoop_experiment" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 1
        p3["height"] = 1
        p3["thickness"] = 12
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")            
            extra = part["kwargs"].get("extra", "")
            if filter in name or filter in extra:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        generate_navigation(sort = sort)

import math

def length_for_volume_mm(radius_mm, total_volume_ml):
    """
    Calculate the length of the cylinder required to achieve the specified volume
    for a shape with two hemispheres and a cylinder.
    
    Args:
        radius_mm (float): The radius of the spheres and the cylinder (in mm).
        total_volume_ml (float): The target total volume of the shape (in mL).
        
    Returns:
        float: The length of the cylindrical part (in mm).
    """
    # Convert radius from mm to cm
    radius_cm = radius_mm * 0.1  # 1 mm = 0.1 cm
    
    # Volume of the two half-spheres (i.e., one full sphere)
    sphere_volume_cm3 = (4 / 3) * math.pi * (radius_cm ** 3)
    
    # Remaining volume for the cylindrical part
    cylinder_volume_cm3 = total_volume_ml - sphere_volume_cm3
    
    # If the cylinder_volume is less than 0, return 0 (impossible to achieve the volume)
    if cylinder_volume_cm3 <= 0:
        return 0
    
    # Length of the cylinder required in cm
    cylinder_length_cm = cylinder_volume_cm3 / (math.pi * (radius_cm ** 2))
    
    # Convert the cylinder length from cm back to mm
    cylinder_length_mm = cylinder_length_cm * 10  # 1 cm = 10 mm
    
    return cylinder_length_mm

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    radius_tbsp = 11
    radius_tsp = 8
    depth_bottom = 1.5
    thickness_wall = 1
    shift_scoop_out = 5
    len_tsp = length_for_volume_mm(radius_tsp, 5)
    len_tbsp = length_for_volume_mm(radius_tbsp, 15)
    extra_base_tsp = 20
    extra_base_tbsp = 5
    
    #add base tbsp
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"    
    wid = len_tbsp + radius_tbsp*2 + thickness_wall + shift_scoop_out + extra_base_tbsp
    hei = radius_tbsp*2 + thickness_wall * 2
    dep = radius_tbsp + depth_bottom
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = radius_tbsp + thickness_wall
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += -wid/2 + extra_base_tbsp
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add base tsp
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"    
    wid = len_tsp + radius_tsp*2 + thickness_wall + shift_scoop_out + extra_base_tsp
    hei = radius_tsp*2 + thickness_wall * 2
    dep = radius_tsp + depth_bottom
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = radius_tsp + thickness_wall
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += wid/2 - extra_base_tsp
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    

    

    
    #add tsp sphere
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"sphere_rectangle"
    #p3["shape"] = f"rounded_rectangle"
    p3["radius"] = radius_tsp
    wid = radius_tsp*2 + len_tsp
    hei = radius_tsp*2
    dep = radius_tsp*2 # /2
    size = [wid, hei, dep]
    p3["size"] = size
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += (len_tsp+radius_tsp*2)/2 + shift_scoop_out
    pos1[2] += depth_bottom
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    
    



    #add tbsp sphere
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"sphere_rectangle"    
    #p3["shape"] = f"rounded_rectangle"
    p3["radius"] = radius_tbsp
    wid = radius_tbsp*2 + len_tbsp
    hei = radius_tbsp*2
    dep = radius_tbsp*2 # /2
    size = [wid, hei, dep]
    p3["size"] = size
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += -(len_tbsp+radius_tbsp*2)/2 - shift_scoop_out
    pos1[2] += depth_bottom
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add m6 hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m6"
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += 0
    
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    
    folder = f"scad_output/{thing['id']}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        opsc.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)  

    yaml_file = f"{folder}/working.yaml"
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id"] = thing["id"]
        part_new["thing"] = thing
        yaml.dump(part_new, file)

def generate_navigation(folder="scad_output", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            #if working.yaml isn't in the root directory, then do it
            if root != folder:
                with open(yaml_file, 'r') as file:
                    part = yaml.safe_load(file)
                    # Process the loaded YAML content as needed
                    part["folder"] = root
                    part_name = root.replace(f"{folder}","")
                    
                    #remove all slashes
                    part_name = part_name.replace("/","").replace("\\","")
                    parts[part_name] = part

                    print(f"Loaded {yaml_file}: {part}")

    pass
    for part_id in parts:
        part = parts[part_id]
        kwarg_copy = copy.deepcopy(part["kwargs"])
        folder_navigation = "navigation_oobb"
        folder_source = part["folder"]
        folder_extra = ""
        for s in sort:
            if s == "name":
                ex = part.get("name", "default")
            else:
                ex = kwarg_copy.get(s, "default")
            folder_extra += f"{s}_{ex}/"

        #replace "." with d
        folder_extra = folder_extra.replace(".","d")            
        folder_destination = f"{folder_navigation}/{folder_extra}"
        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)
        if os.name == 'nt':
            #copy a full directory auto overwrite
            command = f'xcopy "{folder_source}" "{folder_destination}" /E /I /Y'
            print(command)
            os.system(command)
        else:
            os.system(f"cp {folder_source} {folder_destination}")

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)