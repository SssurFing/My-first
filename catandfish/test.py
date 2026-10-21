# import unittest
# import sys
# import io
# from Cels import Cat, Fridge
#
#
# class TestCatAndFridge(unittest.TestCase):
#     def setUp(self):
#         """每条用例执行前，新建独立冰箱，用例完全隔离，无全局污染"""
#         self.fridge = Fridge()
#
#     def test_eat_normal(self):
#         """TC01：正常吃鱼，鱼充足"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#
#         self.fridge.fish_num = 4
#         cat = Cat("Tom", self.fridge)
#         cat._Cat__hungery = 90
#         cat.eat(3)
#
#         self.assertEqual(cat._Cat__hungery, 0)
#         self.assertEqual(self.fridge.fish_num, 1)
#         output = sys.stdout.getvalue()
#         self.assertIn("吃3条鱼，理论减90饥饿度，冰箱剩余1条鱼", output)
#
#         sys.stdout = stdout_backup
#
#     def test_rest(self):
#         """TC02：rest休息，疲劳‑40"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#
#         cat = Cat("Tom2", self.fridge)
#         cat._Cat__fatigued = 100
#         cat.rest()
#
#         self.assertEqual(cat._Cat__fatigued, 60)
#         sys.stdout = stdout_backup
#
#     def test_eat_zero(self):
#         """TC03：eat(0)吃0条鱼"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#
#         self.fridge.fish_num = 5
#         cat = Cat("Tom3", self.fridge)
#         cat._Cat__hungery = 60
#         cat.eat(0)
#
#         self.assertEqual(cat._Cat__hungery, 60)
#         self.assertEqual(self.fridge.fish_num, 5)
#         sys.stdout = stdout_backup
#
#     def test_eat_more_than_stock(self):
#         """TC04：直接调用eat，绕过game_cat交互层判断，鱼变成负数
#         注意：游戏运行时game_cat会做前置判断，不会触发该场景；直接调用类方法会出现负数
#         """
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#
#         self.fridge.fish_num = 2
#         cat = Cat("Tom4", self.fridge)
#         cat._Cat__hungery = 80
#         cat.eat(5)
#
#         self.assertEqual(self.fridge.fish_num, -3)
#         sys.stdout = stdout_backup
#
#     def test_age_up(self):
#         """TC05：age_up，饥饿+10，疲劳+10，年龄+1"""
#         cat = Cat("Tom5", self.fridge)
#         cat._Cat__hungery = 10
#         cat._Cat__fatigued = 10
#         old_age = cat._Cat__age
#         cat.age_up()
#
#         self.assertEqual(cat._Cat__hungery, 20)
#         self.assertEqual(cat._Cat__fatigued, 20)
#         self.assertEqual(cat._Cat__age, old_age + 1)
#
#     def test_life_alive(self):
#         """TC06 life()：饥饿、疲劳都小于100，猫存活返回True"""
#         cat = Cat("Tom6", self.fridge)
#         cat._Cat__hungery = 50
#         cat._Cat__fatigued = 50
#         self.assertEqual(cat.life(), True)
#
#     def test_life_dead_by_hunger(self):
#         """TC07 life()：饥饿>=100，猫死亡返回False"""
#         cat = Cat("Tom7", self.fridge)
#         cat._Cat__hungery = 100
#         cat._Cat__fatigued = 0
#         self.assertEqual(cat.life(), False)
#
#     def test_fishing(self):
#         """TC08 fishing钓鱼：疲劳固定+20，鱼数量增加0‑3之间"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#
#         cat = Cat("Tom8", self.fridge)
#         cat._Cat__fatigued = 0
#         cat.fishing()
#
#         self.assertEqual(cat._Cat__fatigued, 20)
#         # 钓到鱼0~3，断言鱼数量在区间
#         self.assertGreaterEqual(self.fridge.fish_num, 0)
#         self.assertLessEqual(self.fridge.fish_num, 3)
#
#         sys.stdout = stdout_backup
#
#     # --------故意失败用例（演示单元测试失败效果，提交可删除）--------
#     def test_fail_wrong_hunger(self):
#         """TC09【失败】吃鱼后错误断言饥饿=99"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#         self.fridge.fish_num = 4
#         cat = Cat("FailCat1", self.fridge)
#         cat._Cat__hungery = 90
#         cat.eat(3)
#         self.assertEqual(cat._Cat__hungery, 0)
#         sys.stdout = stdout_backup
#
#     def test_fail_rest_wrong_fatigue(self):
#         """TC10【失败】休息错误断言疲劳=100"""
#         stdout_backup = sys.stdout
#         sys.stdout = io.StringIO()
#         cat = Cat("FailCat2", self.fridge)
#         cat._Cat__fatigued = 90
#         cat.rest()
#         self.assertEqual(cat._Cat__fatigued, 50)
#         sys.stdout = stdout_backup
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
import sys
import io
from Cels import Cat, Fridge


class TestCatAndFridge(unittest.TestCase):
    def setUp(self):
        """每条用例执行前，新建独立冰箱，用例完全隔离，无全局污染"""
        self.fridge = Fridge()

    def test_eat_normal(self):
        """TC01：正常吃鱼，鱼充足"""
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        self.fridge.fish_num = 4
        cat = Cat("Tom", self.fridge)
        cat._Cat__hungery = 90
        cat.eat(3)

        self.assertEqual(cat._Cat__hungery, 0)
        self.assertEqual(self.fridge.fish_num, 1)
        output = sys.stdout.getvalue()
        self.assertIn("吃3条鱼，理论减90饥饿度，冰箱剩余1条鱼", output)

        sys.stdout = stdout_backup

    def test_rest(self):
        """TC02：rest休息，疲劳‑40"""
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        cat = Cat("Tom2", self.fridge)
        cat._Cat__fatigued = 100
        cat.rest()

        self.assertEqual(cat._Cat__fatigued, 60)
        sys.stdout = stdout_backup

    def test_eat_zero(self):
        """TC03：eat(0)吃0条鱼"""
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        self.fridge.fish_num = 5
        cat = Cat("Tom3", self.fridge)
        cat._Cat__hungery = 60
        cat.eat(0)

        self.assertEqual(cat._Cat__hungery, 60)
        self.assertEqual(self.fridge.fish_num, 5)
        sys.stdout = stdout_backup

    def test_eat_more_than_stock(self):
        """TC04：直接调用eat，绕过game_cat交互层判断，鱼变成负数
        注意：游戏运行时game_cat会做前置判断，不会触发该场景；直接调用类方法会出现负数
        """
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        self.fridge.fish_num = 2
        cat = Cat("Tom4", self.fridge)
        cat._Cat__hungery = 80
        cat.eat(5)

        self.assertEqual(self.fridge.fish_num, -3)
        sys.stdout = stdout_backup

    def test_age_up(self):
        """TC05：age_up，饥饿+10，疲劳+10，年龄+1"""
        cat = Cat("Tom5", self.fridge)
        cat._Cat__hungery = 10
        cat._Cat__fatigued = 10
        old_age = cat._Cat__age
        cat.age_up()

        self.assertEqual(cat._Cat__hungery, 20)
        self.assertEqual(cat._Cat__fatigued, 20)
        self.assertEqual(cat._Cat__age, old_age + 1)

    def test_life_alive(self):
        """TC06 life()：饥饿、疲劳都小于100，猫存活返回True"""
        cat = Cat("Tom6", self.fridge)
        cat._Cat__hungery = 50
        cat._Cat__fatigued = 50
        self.assertEqual(cat.life(), True)

    def test_life_dead_by_hunger(self):
        """TC07 life()：饥饿>=100，猫死亡返回False"""
        cat = Cat("Tom7", self.fridge)
        cat._Cat__hungery = 100
        cat._Cat__fatigued = 0
        self.assertEqual(cat.life(), False)

    def test_fishing(self):
        """TC08 fishing钓鱼：疲劳固定+20，鱼数量增加0‑3之间"""
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        cat = Cat("Tom8", self.fridge)
        cat._Cat__fatigued = 0
        cat.fishing()

        self.assertEqual(cat._Cat__fatigued, 20)
        # 钓到鱼0~3，断言鱼数量在区间
        self.assertGreaterEqual(self.fridge.fish_num, 0)
        self.assertLessEqual(self.fridge.fish_num, 3)

        sys.stdout = stdout_backup


if __name__ == '__main__':
    unittest.main(verbosity=2)
