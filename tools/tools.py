#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#commap - by jero98772
def writetxt(name,content,mode="w"):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, mode) as file:
    file.write(content)
    file.close()
  m.save(name)
def nullValue(val,newval="-"):
    if not val or val=="":
        return newval 