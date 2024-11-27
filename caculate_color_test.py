if len(circle_index_met) != 0:
    circleindexmet_test = []
    for i in circle_index_met:
        positionpixelcolor = (i[0], i[1])
        pixelcolor = getaveragecolor(positionpixel_color)
        if color_current_position_min <= pixelcolor <= color_current_position_plus:
            draw.point(positionpixelcolor, fill=(0, 255, 0))
            circleindexmet_test.append((x, y))
    nearest_index = min(range(len(circle_index_met_test)), key=lambda i: math.hypot(circle_index_met_test[i][0] - current_position[0], circle_index_met_test[i][1] - current_position[1]))
    nearest_position = circle_index_met_test[nearest_index][0], circle_index_met_test[nearest_index][1]
    distance_between_nearest_current_position = math.sqrt((nearest_position[0] - current_position[0])**2 + (nearest_position[1] - current_position[1])**2)
    if distance_between_nearest_current_position <= (radius + 20):
        pyautogui.moveTo(nearestposition)
    print("show")
