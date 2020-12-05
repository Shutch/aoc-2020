#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        inp.append("")  # need a blank line at the end to signal end of passport
        passport = ""
        valid_passports = 0
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for line in inp:
            if line == "":  # new passport, process old passport
                fields = passport.split(" ")
                keys = [field.split(":")[0] for field in fields]
                keys_present = [field in keys for field in required_fields]
                if all(keys_present):
                    valid_passports += 1
                passport = ""
            elif len(passport) > 0:  # if there's already data, add a space
                passport = passport + " " + line
            else:  # first data for new passport
                passport = passport + line
        return valid_passports


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        inp.append("")  # need a blank line at the end to signal end of passport
        passport = ""
        valid_passports = 0
        for line in inp:
            if line == "":  # new passport, process old passport
                field_list = passport.split(" ")
                fields = {
                    field.split(":")[0]: field.split(":")[1] for field in field_list
                }
                keys = list(fields.keys())
                required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
                keys_present = [field in keys for field in required_fields]
                if all(keys_present):
                    valid_fields = []
                    valid_fields.append(
                        int(fields["byr"]) >= 1920 and int(fields["byr"]) <= 2002
                    )
                    valid_fields.append(
                        int(fields["iyr"]) >= 2010 and int(fields["iyr"]) <= 2020
                    )
                    valid_fields.append(
                        int(fields["eyr"]) >= 2020 and int(fields["eyr"]) <= 2030
                    )

                    # hgt
                    if fields["hgt"][-2:] == "cm":
                        valid_fields.append(
                            int(fields["hgt"][:-2]) >= 150
                            and int(fields["hgt"][:-2]) <= 193
                        )
                    elif fields["hgt"][-2:] == "in":
                        valid_fields.append(
                            int(fields["hgt"][:-2]) >= 59
                            and int(fields["hgt"][:-2]) <= 76
                        )
                    else:
                        valid_fields.append(False)

                    # hcl
                    if fields["hcl"][0] == "#":
                        valid_fields.append(
                            all(
                                [
                                    char in "0123456789abcdef"
                                    for char in fields["hcl"][1:]
                                ]
                            )
                        )
                    else:
                        valid_fields.append(False)

                    valid_fields.append(
                        fields["ecl"]
                        in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    )
                    valid_fields.append(
                        fields["pid"].isnumeric() and len(fields["pid"]) == 9
                    )
                    if all(valid_fields):
                        valid_passports += 1
                passport = ""
            elif len(passport) > 0:  # if there's already data, add a space
                passport = passport + " " + line
            else:  # first data for new passport
                passport = passport + line
        return valid_passports


if __name__ == "__main__":
    day_number = 4
    test_input = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=2,
    )
    part_1.submit_answer()

    test_input = [
        "eyr:1972 cid:100",
        "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
        "",
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:2002 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:2003 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:60in hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:190cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:190in hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:190 hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#123abc ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#123abz ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:123abc ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:brn byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:wat byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:000000001",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:0123456789",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2009 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2031 pid:093154719",
    ]

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer=12,
    )
    part_2.submit_answer()
