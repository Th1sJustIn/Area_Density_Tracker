import math



class EuclideanDistTracker:
    currNum = 0
    currPerson = []


    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0

    def countPerson(self):
        # Initialize variables
        if len(self.currPerson) >= 2:

            previous_value = self.currPerson[0]
            current_value = self.currPerson[len(self.currPerson)-1]
            count = len(self.currPerson)
            negative = 0
            positive = 0

            # Loop through the dataset
            #for current_value in self.currPerson[1:]:  # Start from the second element
            change = current_value[0] - previous_value[0]
            if change > 0:
                positive += 1
            elif change < 0:
                negative += 1
            #previous_value = current_value

            if negative > positive:
                self.currNum -= 1
            elif positive > negative:
                self.currNum += 1
            self.currPerson.clear()

            print("Current student count =" ,self.currNum)

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []


        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 100000:
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    self.currPerson.append([cy])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Track IDs that have left the screen
        left_screen_ids = set(self.center_points.keys())

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center
            # Remove IDs that are still on the screen
            left_screen_ids.discard(object_id)

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()

        # Print "target gone" for IDs that have left the screen
        for id in left_screen_ids:


            self.countPerson()
            print(f"Target {id} gone\n")

        return objects_bbs_ids
