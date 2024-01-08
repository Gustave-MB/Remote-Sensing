# Import libraries
import numpy as np

class SpectralIndices:
    def __init__(self, data):
        """
        Initialize the SpectralIndices class with spectral data.

        Parameters:
        - data (numpy.ndarray): Spectral data (e.g., a 2D array representing an image).
        """
        self.data = data

    def ndvi(self):
        """
        Compute the Normalized Difference Vegetation Index (NDVI).

        Returns:
        - numpy.ndarray: NDVI values.
        """
        red_band = self.data[:, :, 3]  
        nir_band = self.data[:, :, 7]  

        ndvi_values = (nir_band - red_band) / (nir_band + red_band)
        return ndvi_values

    def evi(self):
        """
        Compute the Enhanced Vegetation Index (EVI).

        Returns:
        - numpy.ndarray: EVI values.
        """
        red_band = self.data[:, :, 3] 
        nir_band = self.data[:, :, 7] 
        blue_band = self.data[:, :, 1] 

        evi_values = 2.5 * ((nir_band - red_band) / (nir_band + 6 * red_band - 7.5 * blue_band + 1))
        return evi_values

    def ndwi(self):
        """
        Compute the Normalized Difference Water Index (NDWI).

        Returns:
        - numpy.ndarray: NDWI values.
        """
        green_band = self.data[:, :, 2]  
        nir_band = self.data[:, :, 7] 

        ndwi_values = (green_band - nir_band) / (green_band + nir_band)
        return ndwi_values
    
    def savi(self, L=0.5):
        """
        Compute the Soil-Adjusted Vegetation Index (SAVI).

        Parameters:
        - L (float): Soil brightness correction factor (default is 0.5).

        Returns:
        - numpy.ndarray: SAVI values.
        """
        red_band = self.data[:, :, 3]  
        nir_band = self.data[:, :, 7] 

        savi_values = ((nir_band - red_band) / (nir_band + red_band + L)) * (1 + L)
        return savi_values

    def msi(self):
        """
        Compute the Modified Soil-Adjusted Vegetation Index (MSI).

        Returns:
        - numpy.ndarray: MSI values.
        """
        green_band = self.data[:, :, 2] 
        red_band = self.data[:, :, 3]  
        nir_band = self.data[:, :, 7]  

        msi_values = (nir_band - green_band) / (red_band + green_band)
        return msi_values

    def ci_green(self):
        """
        Compute the Green Chromatic Index (CIgreen).

        Returns:
        - numpy.ndarray: CIgreen values.
        """
        green_band = self.data[:, :, 2]  
        red_band = self.data[:, :, 3]  

        ci_green_values = green_band / red_band
        return ci_green_values
    
    def ndbi(self):
        """
        Compute the Normalized Difference Built-Up Index (NDBI).

        Returns:
        - numpy.ndarray: NDBI values.
        """
        nir_band = self.data[:, :, 7] 
        swir_band = self.data[:, :, 11]  

        ndbi_values = (swir_band - nir_band) / (swir_band + nir_band)
        return ndbi_values



""""
Example usage:
Assume 'image_data' is a 3D numpy array representing spectral bands of an image
For simplicity, let's assume the shape is (height, width, num_bands).
image_data = np.random.rand(100, 100, 10)  # Example random data

spectral_indices_calculator = SpectralIndices(image_data)

ndvi_result = spectral_indices_calculator.ndvi()
evi_result = spectral_indices_calculator.evi()
ndwi_result = spectral_indices_calculator.ndwi()
"""
