#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections, builtins

"""
Programming
Final assignment 4: NS-kaartauatomaat
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""


def inlezen_beginstation(stations):
    """
    De functie vraagt een reiziger om het beginstation van de reis in te voeren. Er wordt
    gecontroleerd of de ingevoerde stationsnaam voorkomt in de meegegeven lijst met stations.

    Het programma blijft vragen om invoer van de gebruiker, totdat een correcte stationsnaam
    (correct == aanwezig in de lijst) is ingevoerd. Deze wordt geretourneerd.

    Args:
        stations (list): Lijst (van strings) met beschikbare stationsnamen
    Returns:
        string: Het gekozen beginstation!
    """
    return


def inlezen_eindstation(stations, beginstation):
    """
    De functie vraagt een reiziger om het eindstation van de reis in te voeren. Er wordt
    gecontroleerd of de ingevoerde stationsnaam voorkomt in de meegegeven lijst met stations.

    Ook wordt gecontroleerd of het eindstation een hogere index in de lijst heeft dan het
    beginstation (eindstation ligt verder op de route).

    Het programma blijft vragen om invoer van de gebruiker, totdat een correcte stationsnaam
    (correct == aanwezig in de lijst & verder op de route dan het beginstation) is ingevoerd.
    Deze wordt geretourneerd.

    Args:
        stations (list): Lijst (van strings) met beschikbare stationsnamen
        beginstation (string): De naam van het station waar de reis begint
    Returns:
        string: Het gekozen eindstation.
    """
    return


def omroepen_reis(stations, beginstation, eindstation):
    """
    Deze functie maakt een string met reisinformatie, en geeft deze als returnwaarde terug!
    Voorbeeld (uitvoer afhankelijk van de parameters):

        Het beginstation Eindhoven is het 11e station in het traject.
        Het eindstation Roermond is het 13e station in het traject.
        De afstand bedraagt 2 station(s).
        De prijs van het kaartje is 10 euro.

        Jij stapt in de trein in: Eindhoven
         - Weert
        Jij stapt uit in: Roermond

    Let op:
     * Het rangnummer (bijv. 11e) is de index van het station (in de lijst met stationsnamen) + 1.
     * Het kost 5 euro om te reizen van een station naar het volgende station.

    In de returnwaarde moeten in dit voorbeeld in ieder geval de volgende 'snippets' voorkomen:
        - '11e station'
        - '13e station'
        - '2 station'
        - '10 euro'

    Args:
        stations (list): Lijst (van strings) met beschikbare stationsnamen
        beginstation (string): De naam van het station waar de reis begint
        eindstation (string): De naam van het station waar de reis eindigt
    Returns:
        string: Het omroepbericht met minimaal de beschreven 'snippets'.
    """
    return


def development_code():
    # Gebruik (delen van) deze code om je functies te testen tijdens het programmeren:
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']

    beginstation = inlezen_beginstation(stations)
    eindstation = inlezen_eindstation(stations, beginstation)
    print(omroepen_reis(stations, beginstation, eindstation))


def module_runner():
    development_code()  # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def test_inlezen_beginstation():
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']

    case = collections.namedtuple('case', 'simulated_input expected_start')
    testcases = [ case(["asfasf", "Schagen", "Alkmaar"], "Schagen"),
                  case(["Sittard" ], "Sittard"),
                  case(["Alkmr", "Alkmeer", "Alkmaar"], "Alkmaar") ]

    for test in testcases:
        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt: simulated_input.pop()

        try:
            beginstation = inlezen_beginstation(stations)
        except IndexError:
            beginstation = 'geen return'
        finally:
            builtins.input = original_input

        assert beginstation == test.expected_start, f"Fout: inlezen_beginstation(<stationslist>) geeft {beginstation} ipv {test.expected_start} (gesimuleerde input: {test.simulated_input})"


def test_inlezen_eindstation():
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']

    case = collections.namedtuple('case', 'simulated_input start expected_stop')
    testcases = [ case(["asfasf", "Schagen", "Maastricht" ], "Schagen", "Maastricht"),
                  case(["asfsdf", "Schagen", "Alkmaar", "asfdfa", "Maastricht" ], "Alkmaar", "Maastricht"),
                  case(["Groningen", "Schagen", "Dedemsvaart", "Zaltbommel" ], "Alkmaar", 'geen return')]

    for test in testcases:
        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop()

        try:
            eindstation = inlezen_eindstation(stations, test.start)
        except IndexError:
            eindstation = 'geen return'
        finally:
            builtins.input = original_input

        assert eindstation == test.expected_stop, f"Fout: inlezen_eindstation(<stationslist>, '{test.start}') geeft {eindstation} ipv {test.expected_stop} (gesimuleerde input: {test.simulated_input})"


def test_omroepen_reis():
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']

    case = collections.namedtuple('case', 'start stop expected_start_rank, expected_stop_rank, expected_distance expected_price')
    testcases = [ case("Schagen", "Maastricht", "1e station", "15e station", "14 station", "70 euro"),
                  case("Alkmaar", "Weert", "3e station", "12e station", "9 station", "45 euro"),
                  case("Heerhugowaard", "Sittard", "2e station", "14e station", "12 station", "60 euro") ]


    for test in testcases:
        omroepbericht = omroepen_reis(stations, test.start, test.stop)
        assert type(omroepbericht) is str, f"Fout: omroepen_reis(<stations>, {test.start}, {test.stop}) levert {omroepbericht} ipv string"

        assertmsg = "Fout: omroepen_reis(<stations>, {}, {}) bevat niet de vereiste {}-tekst '{}'. Jouw returnwaarde: \n<<\n"+omroepbericht+"\n>>"
        assert test.expected_start_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-beginstation', test.expected_start_rank)
        assert test.expected_stop_rank in omroepbericht, assertmsg.format(test.start, test.stop, 'rangnummer-eindstation', test.expected_stop_rank)
        assert test.expected_distance in omroepbericht, assertmsg.format(test.start, test.stop, 'afstand', test.expected_distance)
        assert test.expected_price in omroepbericht, assertmsg.format(test.start, test.stop, 'prijs', test.expected_price)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_inlezen_beginstation, test_inlezen_eindstation, test_omroepen_reis ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()