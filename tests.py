import unittest

from kol1 import Plane_position, Flight

class Koltest(unittest.TestCase):
	
	def test_create_flight_instance_and_get_angle(self):
		instance = Flight()
		self.assertEquals(instance.desired_angle,90)

	def test_Plane_position_create_and_check_mu_values(self):
		instance = Plane_position()
		self.assertEquals(instance.mu,90)

	def test_get_sigma(self):
		instance = Plane_position()
		self.assertEquals(instance.sigma,20)

	def test_get_turbulence_mu(self):
		instance = Flight()
		self.assertEquals(instance.turbulence_mu,0)

	def test_get_turbulence_sigma(self):
		instance = Flight()
		self.assertEquals(instance.turbulence_sigma,2)
	
	def test_get_correction_fraction_after_init(self):
		instance = Flight()
		self.assertAlmostEqual(instance.correction_fraction, 0.5000, places=4)
	
	def test_update_angle_false(self):
		instance = Plane_position()
		old_angle = instance.get_angle()
		instance.update_angle(27.5)
		self.assertNotEqual(instance.get_angle(),old_angle)

	def test_update_angle_true(self):
		instance = Plane_position()
		old_angle = instance.get_angle()
		instance.update_angle(27.5)
		self.assertAlmostEqual(instance.get_angle()-old_angle, 27.5, places=1)

	def test_add_turbulence(self):
		instance = Flight()
		instance.add_turbulence()
		self.assertFalse(abs(instance.position.get_angle()-90.0)<0.00001)

	def test_add_correction(self):
		instance = Flight()
		instance.add_turbulence()
		instance.add_correction()
		self.assertFalse(abs(instance.position.get_angle()-90.0)>0.1)

	
		
	




if __name__ == '__main__':
    unittest.main()
