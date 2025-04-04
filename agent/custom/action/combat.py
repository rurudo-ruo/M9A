import re
import json
import time

from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

from utils import logger


@AgentServer.custom_action("SwitchCombatTimes")
class SwitchCombatTimes(CustomAction):
    """
    选择战斗次数 。

    参数格式:
    {
        "times": "目标次数"
    }
    """

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> CustomAction.RunResult:

        times = json.loads(argv.custom_action_param)["times"]

        context.run_task("OpenReplaysTimes", {"OpenReplaysTimes": {"next": []}})
        context.run_task(
            "SetReplaysTimes",
            {
                "SetReplaysTimes": {
                    "template": [
                        f"Combat/SetReplaysTimesX{times}.png",
                        f"Combat/SetReplaysTimesX{times}_selected.png",
                    ],
                    "order_by": "Score",
                    "next": [],
                }
            },
        )

        return CustomAction.RunResult(success=True)


@AgentServer.custom_action("PsychubeDoubleTimes")
class PsychubeDoubleTimes(CustomAction):
    """
    "识别加成次数，根据结果覆盖 PsychubeVictoryOverrideTask 中参数"
    """

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> CustomAction.RunResult:

        img = context.tasker.controller.post_screencap().wait().get()
        reco_detail = context.run_recognition(
            "PsychubeDouble",
            img,
        )

        if reco_detail is not None:
            text = reco_detail.best_result.text
            pattern = "(\\d)/4"
            times = int(re.search(pattern, text).group(1))
            expected = self._int2Chinese(times)
            context.override_pipeline(
                {
                    "PsychubeVictoryOverrideTask": {
                        "custom_action_param": {
                            "PsychubeFlagInReplayTwoTimes": {"expected": f"{expected}"},
                            "SwitchCombatTimes": {
                                "custom_action_param": {"times": times}
                            },
                            "PsychubeVictory": {
                                "next": ["HomeFlag", "PsychubeVictory"],
                                "interrupt": [
                                    "HomeButton",
                                    "CombatEntering",
                                    "HomeLoading",
                                ],
                            },
                            "PsychubeDouble": {"enabled": False},
                        }
                    }
                }
            )

            return CustomAction.RunResult(success=True)

    def _int2Chinese(self, times: int) -> str:
        Chinese = ["一", "二", "三", "四"]
        return Chinese[times - 1]


@AgentServer.custom_action("TeamSelect")
class TeamSelect(CustomAction):
    """
    队伍选择

    参数格式：
    {
        "team": "队伍选择"
    }
    """

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> CustomAction.RunResult:

        team = json.loads(argv.custom_action_param)["team"]
        target_list = [
            [794, 406],
            [794, 466],
            [797, 525],
            [798, 586],
        ]
        target = target_list[team - 1]

        flag = False
        while not flag:

            img = context.tasker.controller.post_screencap().wait().get()

            if context.run_recognition("TeamlistOpen", img) is not None:
                context.tasker.controller.post_click(target[0], target[1])
                time.sleep(1)
                flag = True
            elif context.run_recognition("TeamlistOff", img) is not None:
                context.tasker.controller.post_click(965, 650)
                time.sleep(1)

        return CustomAction.RunResult(success=True)
