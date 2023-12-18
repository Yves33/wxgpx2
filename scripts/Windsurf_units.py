#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import units
windsurf_units={'lat': {'u_scale': 1.0, 'u_sym': 'deg'}, 
                'lon': {'u_scale': 1.0, 'u_sym': 'deg'}, 
                'distance': {'u_scale': 1.0, 'u_sym': 'm'}, 
                'seconds': {'u_scale': 1.0, 'u_sym': 's'}, 
                'speed': {"u_scale":1.94384,"u_sym":'kts'}, 
                'heading': {'u_scale': 1.0, 'u_sym': 'deg'}, 
                'ele': {'u_scale': 1.0, 'u_sym': 'm'}, 
                'deltat': {'u_scale': 1.0, 'u_sym': 's'}, 
                'deltaxy': {'u_scale': 1.0, 'u_sym': 'm'}, 
                'deltaz': {'u_scale': 1.0, 'u_sym': 'm'}, 
                'ascspeed': {'u_scale': 1.0, 'u_sym': 'm/s'},
                'awaa':{'u_scale': 1.0, 'u_sym': 'deg'},
                'awar':{'u_scale': 1.0, 'u_sym': 'deg'},
                'uwa':{'u_scale': 1.0, 'u_sym': 'deg'},
                'vmg': {"u_scale":1.94384,"u_sym":'kts'}, 
                'aws': {"u_scale":1.94384,"u_sym":'kts'}
                }
units.attrs_load(gpx,windsurf_units)
sync()