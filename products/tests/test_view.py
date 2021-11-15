from .test_setup import TestSetUp


class TestView(TestSetUp):
    def test_product_can_not_created_withot_data(self):
        res = self.client.post(self.products_url)
        self.assertEqual(res.status_code, 400)

    def test_product_creation(self):
        res = self.client.post(self.products_url,self.product_data,format= "multipart")
        # import pdb ;pdb.set_trace()
        self.assertEqual(res.data["name"], self.product_data["name"])
        self.assertEqual(res.status_code, 201)
