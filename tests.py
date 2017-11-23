import unittest

from kol1 import Plane_position, Flight

class Koltest(unittest.TestCase):
	
	def test_create_flight_instance_and_get_angle(self):
		instance = Flight()
		self.assertEuqals(instance.desired_angle,0)

	def test_Plane_position_create_and_check_mu_values(self):
		instance = Plane_position()
		self.assertEuqals(instance.mu,90)

	def test_get_sigma(self):
		instance = Plane_position()
		self.assertEuqals(instance.sigma,20)

	def test_get_turbulence_mu(self):
		instance = Flight()
		self.assertEuqals(instance.turbulence_mu,0)

	def test_get_turbulence_sigma(self):
		instance = Flight()
		#self.assertEuqals(instance.turbulence_sigma,2)
	
	def test_get_correction_fraction_after_init(self):
		pass
	




if __name__ == '__main__':
    unittest.main()
