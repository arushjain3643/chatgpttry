import unittest

from simulator import available_choices, simulate


class SimulatorTests(unittest.TestCase):
    def test_available_choices_expected(self):
        self.assertEqual(
            available_choices(),
            ["confess_crush", "drop_out", "move_city", "start_business"],
        )

    def test_simulate_returns_requested_sample_count(self):
        runs = simulate("move_city", samples=3, seed=7)
        self.assertEqual(len(runs), 3)

    def test_simulate_deterministic_with_seed(self):
        first = simulate("start_business", samples=4, seed=11)
        second = simulate("start_business", samples=4, seed=11)
        self.assertEqual(first, second)

    def test_simulate_rejects_invalid_choice(self):
        with self.assertRaises(ValueError):
            simulate("become_astronaut", samples=1)

    def test_simulate_rejects_invalid_samples(self):
        with self.assertRaises(ValueError):
            simulate("drop_out", samples=0)


if __name__ == "__main__":
    unittest.main()
