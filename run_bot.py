#!/usr/bin/env python3
import os
import sys

# Ana dizini Python path'e ekle
sys.path.insert(0, '.')

# Ana dizine geçiş yap  
os.chdir('.')

# FallenMusic main dosyasını çalıştır
exec(open('FallenMusic/__main__.py').read())