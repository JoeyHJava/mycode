#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Garage',
                  # 'item'  : {{'noun':'laptop', 'verb': 'I love python'}, 'mail', 'key'},
                  'item'  : {'laptop': {'desc': 'I love python'},'mail': {'desc': '...mail description'}, 'key': {'desc': 'device to open things'}},
                  'description': 'you are in hall...deal with it'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'description': 'you are in kitchen. Good time for a snack'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'description': 'entering the dinning room.. or is it the dying room muHaHa'

               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'west' : 'Gym',
                  'item': 'phone',
                  'description': 'someone needs to take better care of their garden'

               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
                  'description': 'this pantry sucks. Why does a kitchen need a closet?'
            },
            'Gym' : {
                  'north' : 'Garage',
                  'east' : 'Garden',
                  'item' : 'health',
                  'description': 'nice gym, someone crossfits!'
            },
            'Garage' : {
                  'east' : 'Hall',
                  'item' : 'health',
                  'description': 'this garage is hella clutter. A monster could be hiding anywhere in here!'
            }
         }
