"""Every remaining topic game has ten real trials, not the discovery card."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "science_playground"
sys.path.insert(0, str(ROOT))

from lessons.catalog import validate_catalog
from pair_trials import flip_two_choice, named_trials, step_trials
from picture_scenes import EXTRA_SCENES
from science_utils import _BESPOKE_GAMES, _with_discovery_trials

from modules import follow_the_steps_advanced as fts_adv
from modules import follow_the_steps_beginner as fts_beg
from modules import follow_the_steps_intermediate as fts_int
from modules import forces_stuff_advanced as forces_adv
from modules import forces_stuff_intermediate as forces_int
from modules import light_sound_advanced as light_adv
from modules import light_sound_intermediate as light_int
from modules import living_things_advanced as living_adv
from modules import living_things_beginner as living_beg
from modules import living_things_intermediate as living_int
from modules import make_test_advanced as make_adv
from modules import make_test_beginner as make_beg
from modules import make_test_intermediate as make_int
from modules import matter_advanced as matter_adv
from modules import matter_beginner as matter_beg
from modules import matter_intermediate as matter_int
from modules import motion_advanced as motion_adv
from modules import motion_intermediate as motion_int

DISCOVERY_PLACES = {
    "Beach", "Garden", "Music room", "Bridge bench", "Robot mat",
    "Ice tray", "Playground", "Balance table", "Sunny yard",
}

GIVEAWAY = (
    "FAST", "SLOW", "LOUD", "QUIET", "HIGH", "LOW",
    "FARTHER", "SPEEDING UP", "UPHILL", "DOWNHILL",
    "SPLASH", "MELT",
)

COMPARE_BANKS = (
    ("forces_stuff_intermediate_balance_the_seesaw", forces_int.BALANCE, "Who sits near the middle?", "Who sits far away?", "compare"),
    ("forces_stuff_intermediate_will_it_slide", forces_int.SLIDE, "Which floor lets the box slide?", "Which floor holds the box?", "compare"),
    ("forces_stuff_intermediate_stronger_push_wins", forces_int.PUSH, "Which push wins?", "Which push loses?", "compare"),
    ("light_sound_intermediate_make_a_shadow", light_int.SHADOW, "What makes a shadow?", "What does not make a shadow?", "compare"),
    ("light_sound_intermediate_which_is_louder", light_int.LOUDER, "Which wave looks louder?", "Which wave looks quieter?", "compare"),
    ("light_sound_intermediate_echo_or_no_echo", light_int.ECHO, "Where will you hear an echo?", "Where will the sound stay quiet?", "compare"),
    ("matter_intermediate_ice_to_water", matter_int.ICE, "Which one turns to water?", "Which one stays frozen?", "compare"),
    ("matter_intermediate_same_stuff_new_look", matter_int.SAME, "Which pair is the same stuff?", "Which pair is different stuff?", "compare"),
    ("matter_intermediate_mix_or_settle", matter_int.MIX, "Which mix settles apart?", "Which mix stays mixed?", "compare"),
    ("living_things_intermediate_what_does_it_need", living_int.NEEDS, "What helps this living thing grow?", "What does not help it grow?", "compare"),
    ("living_things_intermediate_who_eats_what", living_int.EATS, "What should it eat?", "What is not food?", "compare"),
    ("living_things_intermediate_home_habitat", living_int.HOME, "Where does it belong?", "Where does it not belong?", "compare"),
    ("make_test_intermediate_test_the_bridge", make_int.BRIDGE, "Which test checks the bridge?", "Which does not test the bridge?", "compare"),
    ("make_test_intermediate_fix_the_ramp", make_int.RAMP, "What should change to help the car?", "What makes the car stop early?", "compare"),
    ("make_test_intermediate_predict_then_try", make_int.PREDICT, "What comes after predict?", "What skips the test?", "compare"),
    ("motion_advanced_steeper_goes_faster", motion_adv.STEEP, "Which ramp makes more speed?", "Which ramp stays slow?", "compare"),
    ("motion_advanced_two_pushes_add_up", motion_adv.PUSHES, "Which way do the pushes add?", "Which way loses?", "compare"),
    ("motion_advanced_race_the_clock", motion_adv.CLOCK, "Same trip. Who is faster?", "Same trip. Who is slower?", "compare"),
    ("forces_stuff_advanced_fair_balance", forces_adv.FAIR, "What keeps both sides even?", "What tips the seesaw?", "compare"),
    ("forces_stuff_advanced_rough_vs_smooth_ramp", forces_adv.ROUGH, "Which ramp lets the car go farther?", "Which ramp stops the car sooner?", "compare"),
    ("forces_stuff_advanced_lift_with_a_lever", forces_adv.LEVER, "Where should the pivot go?", "Where makes lifting harder?", "compare"),
    ("light_sound_advanced_bigger_block_bigger_shadow", light_adv.BLOCK, "Which makes the bigger shadow?", "Which makes the smaller shadow?", "compare"),
    ("light_sound_advanced_pitch_ladder", light_adv.PITCH, "Which note has the highest pitch?", "Which note has the lowest pitch?", "compare"),
    ("light_sound_advanced_light_path_blocked", light_adv.PATH, "What blocks the light?", "What lets the light through?", "compare"),
    ("matter_advanced_water_cycle_pictures", matter_adv.CYCLE, "What comes after a rain puddle warms?", "What needs cold instead?", "compare"),
    ("matter_advanced_soft_to_hard", matter_adv.HARD, "Which one gets harder?", "Which one stays soft?", "compare"),
    ("matter_advanced_what_holds_shape", matter_adv.SHAPE, "Which keeps its own shape?", "Which can splash or spill?", "compare"),
    ("living_things_advanced_day_and_night_animals", living_adv.NIGHT, "Which animal is awake at night?", "Which animal likes the day?", "compare"),
    ("living_things_advanced_help_it_grow", living_adv.GROW, "Plant is pale. What should change?", "What makes the pale plant worse?", "compare"),
    ("make_test_advanced_stronger_shape", make_adv.SHAPE, "Which shape makes a strong frame?", "Which shape is floppy?", "compare"),
    ("make_test_advanced_two_tests_pick_better", make_adv.BETTER, "Which one did better on the test?", "Which one did worse?", "compare"),
    ("make_test_advanced_build_a_path", make_adv.PATH, "Gap blocks the marble. Add what?", "What is too soft for the gap?", "compare"),
    ("matter_beginner_solid_or_splash", matter_beg.SOLID_SPLASH, "Which one can splash?", "Which one holds its shape?", "solid_or_splash"),
    ("matter_beginner_hot_or_cold", matter_beg.HOT_COLD, "Which one feels cold?", "Which one feels hot?", "hot_or_cold"),
    ("living_things_beginner_living_or_not", living_beg.LIVING, "Which one is living?", "Which one is not living?", "living_or_not"),
    ("living_things_beginner_plant_or_animal", living_beg.PLANT_ANIMAL, "Which one is a plant?", "Which one is an animal?", "plant_or_animal"),
    ("living_things_beginner_hungry_or_full", living_beg.HUNGRY, "What does the hungry one need?", "What does the hungry one not need?", "hungry_or_full"),
    ("motion_intermediate_who_went_farther", motion_int.FARTHER, "Which one went farther?", "Which one stopped sooner?", "compare"),
)

STEP_BANKS = (
    ("follow_the_steps_beginner_first_then_next", fts_beg.FIRST_NEXT, "first_then_next"),
    ("follow_the_steps_beginner_which_step_is_missing", fts_beg.MISSING, "missing_step"),
    ("follow_the_steps_beginner_do_it_again", fts_beg.AGAIN, "do_it_again"),
    ("matter_beginner_melt_or_freeze", matter_beg.MELT_FREEZE, "melt_or_freeze"),
    ("motion_intermediate_speeding_up", motion_int.SPEED, "speeding_up"),
    ("motion_intermediate_which_way_does_it_roll", motion_int.ROLL, "roll_downhill"),
    ("follow_the_steps_intermediate_three_step_robot", fts_int.ROBOT, "first_then_next"),
    ("follow_the_steps_intermediate_if_red_then_stop", fts_int.IFTHEN, "first_then_next"),
    ("follow_the_steps_intermediate_repeat_3_times", fts_int.REPEAT, "do_it_again"),
    ("living_things_advanced_life_cycle_order", living_adv.CYCLE, "first_then_next"),
    ("follow_the_steps_advanced_debug_the_path", fts_adv.DEBUG, "missing_step"),
    ("follow_the_steps_advanced_loop_the_square", fts_adv.SQUARE, "do_it_again"),
    ("follow_the_steps_advanced_if_wet_then_boots", fts_adv.WET, "first_then_next"),
)

NAMED_BANKS = (
    ("make_test_beginner_will_the_tower_fall", make_beg.TOWERS, "tower_fall", "Which tower will stay up?", "Which tower will fall?"),
    ("make_test_beginner_ramp_or_wall", make_beg.RAMPS, "ramp_or_wall", "Which helps it roll down?", "Which stops it?"),
    ("make_test_beginner_fit_the_hole", make_beg.HOLES, "fit_the_hole", "Which shape fits the round hole?", "Which shape does not fit?"),
)


def _all_banks() -> list[tuple[str, tuple]]:
    banks = []
    for game_id, pairs, q_a, q_b, scene in COMPARE_BANKS:
        banks.append((game_id, flip_two_choice(pairs, a="a", b="b", q_for_a=q_a, q_for_b=q_b, scene=scene)))
    for game_id, rows, scene in STEP_BANKS:
        banks.append((game_id, step_trials(rows, scene)))
    for game_id, rows, scene, q_a, q_b in NAMED_BANKS:
        banks.append((game_id, named_trials(rows, scene, q_a, q_b)))
    return banks


def test_catalog_still_valid() -> None:
    validate_catalog()


def test_every_bank_has_ten_unique_questions_and_no_discovery() -> None:
    seen_ids = []
    for game_id, trials in _all_banks():
        seen_ids.append(game_id)
        assert game_id in _BESPOKE_GAMES, game_id
        assert len(trials) == 10, (game_id, len(trials))
        questions = [trial["question"] for trial in trials]
        assert questions[0] != questions[1], (game_id, questions[:2])
        for trial in trials:
            assert trial["answer"] in trial["choices"], (game_id, trial)
            assert trial.get("context") not in DISCOVERY_PLACES
            assert trial.get("scene") != "discovery"
        wrapped = _with_discovery_trials({
            "id": game_id,
            "question": trials[0]["question"],
            "choices": list(trials[0]["choices"]),
            "answer": trials[0]["answer"],
            "tip": "tip",
            "trials": trials,
        })
        assert all(trial.get("context") not in DISCOVERY_PLACES for trial in wrapped["trials"])
        assert {trial.get("scene") for trial in wrapped["trials"]} != {"discovery"}
    assert len(seen_ids) == len(set(seen_ids))


def test_compare_and_step_scenes_use_names_not_giveaway_tags() -> None:
    html = EXTRA_SCENES["compare"](
        0,
        {
            "left_name": "Heavy bear",
            "right_name": "Light bunny",
            "left_pic": "🐻",
            "right_pic": "🐰",
            "left_move": "still",
            "right_move": "bob",
        },
        pose="play",
    )
    assert "Heavy bear" in html and "Light bunny" in html
    assert "Beach" not in html
    assert "FAST" not in html

    farther = EXTRA_SCENES["who_went_farther"](
        0, {"near_name": "Blue car", "far_name": "Red car"}, pose="play",
    )
    assert "Blue car" in farther and "Red car" in farther
    assert "FARTHER" not in farther

    speed = EXTRA_SCENES["speeding_up"](
        0, {"vehicle": "Race car", "gaps": "grow"}, pose="play",
    )
    assert "Race car" in speed
    assert "SPEEDING UP" not in speed

    roll = EXTRA_SCENES["roll_downhill"](
        0, {"ball": "Soccer ball", "ball_pic": "⚽"}, pose="play",
    )
    assert "Soccer ball" in roll
    assert "UPHILL" not in roll and "DOWNHILL" not in roll

    melt = EXTRA_SCENES["melt_or_freeze"](
        0, {"stuff": "Ice", "stuff_pic": "🧊", "action": "melt"}, pose="play",
    )
    assert "Ice" in melt
    assert "it melts" not in melt


def test_first_then_next_asks_what_comes_next() -> None:
    wash = fts_beg.FIRST_NEXT[1]
    assert wash["question"] == "First wash hands. What comes next?"
    assert wash["answer"] == "Soap"
    assert "extra" not in wash["question"].lower()
    for row in fts_beg.FIRST_NEXT:
        assert "What comes next?" in row["question"]
        assert "extra" not in row["question"].lower()


def test_first_then_next_car_round_shows_a_seatbelt() -> None:
    row = fts_beg.FIRST_NEXT[7]
    assert row["answer"] == "Seatbelt"
    assert "Buckle" not in row["choices"]
    assert "sit in the car" in row["question"]
    html = EXTRA_SCENES["first_then_next"](7, row, pose="start")
    assert "car-seat" in html
    assert "belt-buckle" in html
    assert "Seatbelt" in html
    assert "🔒" not in html
