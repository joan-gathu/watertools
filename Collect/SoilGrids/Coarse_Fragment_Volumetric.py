# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels
Module: Collect/SoilGrids
"""
import os
from watertools.Collect.SoilGrids.DataAccess import DownloadData
import sys


def main(Dir, latlim, lonlim, level = 'sl1', Waitbar = 1):
    """
    Downloads SoilGrids data from ftp://ftp.soilgrids.org/data/recent/

    The following keyword arguments are needed:
    Dir -- 'C:/file/to/path/'
    latlim -- [ymin, ymax]
    lonlim -- [xmin, xmax]
    level -- 'sl1' (Default) 
             'sl2'     
             'sl3'     
             'sl4'     
             'sl5'     
             'sl6'     
             'sl7'    
    Waitbar -- '1' if you want a waitbar (Default = 1)
    """

    # Create directory if not exists for the output
    output_folder = os.path.join(Dir, 'SoilGrids', 'Coarse_Fragment_Volumetric')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the output map and create this if not exists
    nameEnd = os.path.join(output_folder, 'CoarseFragmentVolumetric_%s_SoilGrids_percentage.tif' %level)     

    if not os.path.exists(nameEnd):

        # Create Waitbar
        if Waitbar == 1:
            print('\nDownload Coarse Fragment Volumetric soil map of %s from SoilGrids.org' %level)
            import watertools.Functions.Random.WaitbarConsole as WaitbarConsole
            total_amount = 1
            amount = 0
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # Download and process the data
        DownloadData(output_folder, latlim, lonlim, "CRFVOL", level)

        if Waitbar == 1:
            amount = 1
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    else:
        if Waitbar == 1:
            print("\nCoarse Fragment Volumetric soil map of %s from SoilGrids.org already exists in output folder" %level)

if __name__ == '__main__':
    main(sys.argv)

