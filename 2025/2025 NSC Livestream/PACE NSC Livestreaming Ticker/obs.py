import config

def toggle_source_visibility(scene_name, source_name, visibility):
    try:
        # Get scene item ID for the source
        response = config.ws.call(config.obswebsocket.requests.GetSceneItemId(sceneName=scene_name, sourceName=source_name))
        scene_item_id = response.getSceneItemId()

        # Hide the source
        config.ws.call(config.obswebsocket.requests.SetSceneItemEnabled(sceneName=scene_name, sceneItemId=scene_item_id, sceneItemEnabled=visibility))

    except Exception as e:
        print(f"Failed to connect or perform actions: {source_name}")

def move_source_X(scene_name, source_name, x_POS):
    try:

        response = config.ws.call(config.obswebsocket.requests.GetSceneItemId(sceneName=scene_name, sourceName=source_name))
        scene_item_id = response.getSceneItemId()

        transform = {'positionX':x_POS}

        # Adjust the position
        response = config.ws.call(config.obswebsocket.requests.SetSceneItemTransform(sceneName=scene_name, sceneItemId=scene_item_id, sceneItemTransform=transform))

    except Exception as e:
        print(f"Error {e}")

def move_source_Y(scene_name, source_name, y_POS):
    try:
        response = config.ws.call(config.obswebsocket.requests.GetSceneItemId(sceneName=scene_name, sourceName=source_name))
        scene_item_id = response.getSceneItemId()

        transform = {'positionY':y_POS}

        # Adjust the position
        response = config.ws.call(config.obswebsocket.requests.SetSceneItemTransform(sceneName=scene_name, sceneItemId=scene_item_id, sceneItemTransform=transform))

    except Exception as e:
        print(f"Error {e}")

def toggle_ticker_opacity(scene_name, source_name, filter_name, opacity):
    try:
        uuid=get_uuid(scene_name)

        response = config.ws.call(config.obswebsocket.requests.GetSourceFilter(sourceName=source_name, sourceUuid=uuid, filterName=filter_name))
        print(response)

        filter_settings = {'opacity':opacity}
        print(filter_settings)

        # Apply the updated settings
        response = config.ws.call(config.obswebsocket.requests.SetSourceFilterSettings(sourceName=source_name, sourceUuid=uuid, filterName=filter_name, filterSettings=filter_settings))
        print(response)

    except Exception as e:
        print(f"Error {e}")

def set_scene(scene_name):
    uuid = get_uuid(scene_name)
    response = config.ws.call(config.obswebsocket.requests.SetCurrentProgramScene(sceneName=scene_name, sceneUuid=uuid))
    #print(response)

def get_uuid(scene_name):
    print(scene_name)

    response = config.ws.call(config.obswebsocket.requests.GetSceneList())
    scenes = response.getScenes()
    
    for scene in scenes:
        if scene['sceneName'] == scene_name:
            return scene['sceneUuid']

    return 0

def set_phase(phase):
    path = "./Text Files/Game Room/Active Phase.txt"
    with open(path, 'w') as file:
        file.write(phase)

def set_round(round):

    rnd = "Round"

    if(not rnd in round):
        round = rnd + " " + round

    path = "./Text Files/Game Room/Current Round.txt"
    with open(path, 'w') as file:
        file.write(round)

def test(scene_name, source_name):
    uuid = get_uuid(scene_name)
    response = config.ws.call(config.obswebsocket.requests.GetSceneItemList(scene_name=scene_name, sceneUuid=uuid))
    print(response)

def centerText(text, scene_name, text_source, box_source):
    try:
        print(text)

        response = config.ws.call(config.obswebsocket.requests.GetSceneItemId(sceneName=scene_name, sourceName=text_source))
        text_scene_item_id = response.getSceneItemId()

        response = config.ws.call(config.obswebsocket.requests.GetSceneItemId(sceneName=scene_name, sourceName=box_source))
        box_scene_item_id = response.getSceneItemId()

        uuid = get_uuid(scene_name)

        response = config.ws.call(config.obswebsocket.requests.GetSceneItemTransform(scene_name=scene_name, sceneUuid=uuid, sceneItemId=text_scene_item_id))
        print(response.getSceneItemTransform())
        text_stats = response.getSceneItemTransform()

        response = config.ws.call(config.obswebsocket.requests.GetSceneItemTransform(scene_name=scene_name, sceneUuid=uuid, sceneItemId=box_scene_item_id))
        print(response.getSceneItemTransform())
        box_stats = response.getSceneItemTransform()

        x, y = place_coords(text, get_font(scene_name, text), get_bold(scene_name, text), box_stats['width'], box_stats['height'])
        x = x + box_stats['positionX']
        y = y + box_stats['positionY']

        print(f"Place text at: ({x}, {y})")
        print("--------------------------")

        move_source_X(scene_name, text_source, x)
        #move_source_Y(scene_name, text_source, y)

    except Exception as e:
        print(f"Error {e}")

def place_coords(text, font_size, is_bold, box_width, box_height):

    # Load the font
    font_path = "./Fonts/arialbd.ttf" if is_bold else "./Fonts/arial.ttf"  # Replace with your font path
    try:
        font = config.ImageFont.truetype(font_path, font_size)
    except OSError:
        raise ValueError("Font file not found. Ensure you have the appropriate font file.")

    # Measure the text size
     # Create a dummy image and draw object to measure the text
    dummy_image = config.Image.new("RGB", (1, 1))
    draw = config.ImageDraw.Draw(dummy_image)

    # Measure the text bounding box
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the top-left corner position to center the text
    x = (box_width - text_width) // 2
    y = (box_height - text_height) // 2

    return x, y

def get_font(scene, text):
    if scene == "Full Screen - Individual - Background":
        return 32
    elif scene == config.FSS_BRACKETS_3_8TEAMS or scene == config.FSS_BRACKETS_3_6TEAMS:
        return 40
    elif scene == config.FSS_INDIVIDUAL:
        if str(text).find("PPG") != -1:
            return 48
        else:
            return 56

def get_bold(scene, text):
    if scene == "Full Screen - Individual - Background":
        return True
    elif scene == config.FSS_BRACKETS_3_8TEAMS or scene == config.FSS_BRACKETS_3_6TEAMS:
        return True
    elif scene == config.FSS_INDIVIDUAL:
        return True

def ping():
    return True

if __name__ == "__main__":
    config.init()
    #test("Full Screen - Brackets - 8 Teams - One", "")
    #x, y = place_coords("Player", 32, True, 560,40)
    #print(f"Place text at: ({x}, {y})")
    centerText("Team","Full Screen - Individual - Background","FS - Individual - Header - Team - Text","FS - Individual - Header - Team - BG")
