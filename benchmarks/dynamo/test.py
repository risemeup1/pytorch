import os
import unittest

from .common import parse_args, run

from .torchbench import setup_torchbench_cwd, TorchBenchmarkRunner


class TestDynamoBenchmark(unittest.TestCase):
    def test_benchmark_infra_runs(self) -> None:
        """
        Basic smoke test that TorchBench runs.

        This test is mainly meant to check that our setup in fbcode
        doesn't break.

        If you see a failure here related to missing CPP headers, then
        you likely need to update the resources list in:
            //caffe2:inductor
        """
        original_dir = setup_torchbench_cwd()
        try:
            args = parse_args(
                [
                    "-dcpu",
                    "--inductor",
                    "--performance",
                    "--only=BERT_pytorch",
                    "-n1",
                    "--batch_size=1",
                ]
            )
            run(TorchBenchmarkRunner(), args, original_dir)
        finally:
            os.chdir(original_dir)
