from dotenv import load_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


playlist = [
    {
        "FirstName": "Allan",
        "LastName": "Taylor",
        "CustomPlaylist": [
            {
                "Name": "Grounding/Clearing",
                "Seconds": 10
            },
            {
                "Name": "Abundance & Prosperity",
                "Seconds": 10
            },
            {
                "Name": "Allan",
                "Seconds": 10
            },
            {
                "Name": "Arteries/Veins/Blood",
                "Seconds": 10
            },
            {
                "Name": "Back Pain",
                "Seconds": 10
            },
            {
                "Name": "Heavy Metals",
                "Seconds": 10
            },
            {
                "Name": "Immune System",
                "Seconds": 10
            },
            {
                "Name": "Male Reproductive",
                "Seconds": 10
            },
            {
                "Name": "Memory",
                "Seconds": 10
            },
            {
                "Name": "Muscles",
                "Seconds": 10
            },
            {
                "Name": "Parasites/Mold/Fungus",
                "Seconds": 10
            },
            {
                "Name": "Stress",
                "Seconds": 10
            },
            {
                "Name": "Virus",
                "Seconds": 10
            },
            {
                "Name": "Wellness",
                "Seconds": 10
            },
        ],
        "Homeppathics":  [
            {
                "Name": "Addiction - Alcohol Addiction / Withdrawal", 
                "Seconds": 10
            },
            {
                "Name": "Addiction - Drug Addiction Treatment / Withdrawal",
                "Seconds": 10
            },
            {
                "Name": "Allergies - Outdoor Allergies",
                "Seconds": 10
            },
            {
                "Name": "Alzheimer's - Problem of the Mind - Memory Weakness",
                "Seconds": 10
            }, 
            {
                "Name": "Brain Fog",
                "Seconds": 10
            },
            {
                "Name": "Dandruff",
                "Seconds": 10
            },
            {
                "Name": "Ears",
                "Seconds": 10
            },
            {
                "Name": "Eyes - Eye Floaters",
                "Seconds": 10
            },
            {
                "Name": "Heart Disease",
                "Seconds": 10
            },
            {
                "Name": "Insect Bites",
                "Seconds": 10
            },
            {
                "Name": "Libido - Low Libido, Infertility or Poor Sperm Quality in Men",
                "Seconds": 10
            },
            {
                "Name": "Liver - Cirrhosis, Liver Detox",
                "Seconds": 10
            },
            {
                "Name": "Liver - Detox",
                "Seconds": 10
            },
            {
                "Name": "Liver - Disease, High Bilirubin Levels",
                "Seconds": 10
            },
            {
                "Name": "Liver - Fatty Liver",
                "Seconds": 10
            },
            {
                "Name": "Liver - Support and Correction",
                "Seconds": 10
            },
            {
                "Name": "Memory Decline",
                "Seconds": 10
            },
            {
                "Name": "Miasms",
                "Seconds": 10
            },
            {
                "Name": "Parasites",
                "Seconds": 10
            },
            {
                "Name": "Parasites / Worms",
                "Seconds": 10
            },
            {
                "Name": "Teeth - Strong Teeth",
                "Seconds": 10
            },
            {
                "Name": "Teeth - Symptoms and Dental Remedies",
                "Seconds": 10
            },
            {
                "Name": "Teeth - Temporomandibular Joint (TMJ)",
                "Seconds": 10
            },
        ],
        "AOTuneBinauralTones": {
            "Gamma": True,
            "Schumann": True,
        },
        "AOTunePlanetaryFrequencies": {
            "Centering": False,
            "FlowerofLife_AlleviatePain_RelaxMuscles_Stress": True,
            "Earth_Om_Relaxing_Soothing_Balancing": True,
            "Pluto_GroupDynamics": True,
            "Mercury_IntellectualCommunication": True,
            "Mars_Focused Energy_StrengthOfWill": True,
            "Saturn_BecomingAware_Concentration": True,
            "GeomagneticField_ImmuneSupport": True,
            "HydrogenGamma_Memory_Attention_Awareness": True,
            "Earth_PlatonicYear_ClarityOfSpirit_Cheerfulness": True,
            "Chiron_Strength_Compassion_Wisdom": True,
            "Sedna_ATPProduction_Oxygenation": False,
            "Jupiter_CreativePower": True,
            "CulminationCycle_ReduceAnxiety_Grounding": False,
            "EarthSynodicDay_Dynamic_Vitalizing": True,
            "EarthSiderealDay_ImproveNervousSystem": True,
            "Uranus_Surprise_Renewal": True,
            "MoonSynodic_SexualEnergyandCommunication": True,
            "Neptune_Intuition_DreamExperience": True,
            "Venus_SkinandHairRejuvenation": True,
            "MoonSidereal_ImprovesSexualEnergy": True,
            "MetonicCycle_ImprovesReproductiveFunction": True,
            "MoonKnot_MaintainsEmotionalBalance": True,
            "SarosPeriod_ImprovesReproductiveFunction": True,
            "ApsidisRotation_Focus_Meditation_Prayer": True,
            "SchumannResonance_EnhancedLearning_Memory": True,
        },
        "AOTunePlanetaryChakraFrequencies": {
            "SolarPlexus,_Power_Sun": True,
            "Heart_Earth_Om_Love": True,
            "Throat_Mercury_Communication": True,
            "Crown_EarthPlatonicYear_Spirituality": True,
            "Root_EarthSynodicDay_Survival": True,
            "Sacral_MoonSynodic_Sexuality": True,
            "ThirdEye_Venus_Intuition": True,
        },
        "AOTuneSolfeggioChakraFrequencies": {
            "Crown_TI_Spirituality": True,
            "ThirdEye_SOL_Expression": True,
            "Throat_FA_Relationships": True,
            "Heart_MI_DNARepair": True,
            "SolarPlexus_RE_UndoingSituationsandFacilitatingChange": True,
            "Sacral_UT_LiberatingGuiltandFear": True,
            "Root_VI_Energy_Rejuvenation": True,
            "Sky_EA_ReducePain_AlleviateStress": False,
            "NoteC_DO_Centering": False,
        },
        "AOTuneOrgans": {
            "Adrenals": False,
            "Bladder": False,
            "Blood": True,
            "Brain": True,
            "Colon": False,
            "FatCells": False,
            "GallBladder": False,
            "Heart": True,
            "Intestines": False,
            "Kidneys": False,
            "Liver": True,
            "Lungs": False,
            "MuscleCells": False,
            "Pancreas": False,
            "Stomach": False,

        },
        "AOTuneDNAandRNA": {
            "DNA_Guanine": False,
            "DNA_Cytosine": False,
            "RNA_Thymine": False,
            "DNA_Adenine": False,
            "RNA_Phenylalanine": False,
            "RNA_Uracil": False,
        },
        "AOTuneSpiritualInsights": {
            "PinealGland": True,
            "SpiritualAwakening1": True,
            "SpiritualAwakening2": False,
            "SpiritualAwakening3": False,
        },
        "AOTuneOttoClearningandConnecting": {
            "OTTOClearingandConnecting1": False,
            "OTTOClearingandConnecting2": False,
            "OTTOClearingandConnecting3": False,
            "OTTOClearingandConnecting4": False,
        },
    }
]

load_dotenv(dotenv_path='.env')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # 1. go to the login page
    driver.get("https://app.aoscan.com")

    # 2. click the “Sign In” button
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

    # 3. log in
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(os.getenv("AO_USERNAME"))
    driver.find_element(By.NAME, "password").send_keys(os.getenv("AO_PASSWORD"))
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    for client in playlist:
        
        # 4. once logged in, select the user profile dropdown/button
        wait.until(EC.element_to_be_clickable((By.ID, "name"))).click()

        # 5. click “Search Existing Clients”
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnExistingUser > span"))).click()

        # 6. fill in last and first name
        wait.until(EC.visibility_of_element_located((By.ID, "lastName"))).click()
        driver.find_element(By.ID, "lastName").clear()
        driver.find_element(By.ID, "lastName").send_keys(client["LastName"])
        driver.find_element(By.ID, "firstName").click()
        driver.find_element(By.ID, "firstName").clear()
        driver.find_element(By.ID, "firstName").send_keys(client["FirstName"])

        # 7. click search and wait for results
        driver.find_element(By.ID, "btnSearch").click()
        first_result_locator = (By.CSS_SELECTOR, ".ao-v2-search-client-li:nth-child(1) > .d-flex")
        wait.until(EC.element_to_be_clickable(first_result_locator)).click()

        # 8. navigate to “Sefi”
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(10) > span"))).click()

        # 9. navigate to “Custom Playlist”
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gap-4 > .btn:nth-child(1)"))).click()

        # 10. for each loop of playlists
        for playlist in client["CustomPlaylist"]:

            # 11. click the dropdown box
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-control:nth-child(1)"))).click()
            dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-control:nth-child(1)")))
            time.sleep(1)

            # 12. select the playlist
            dropdown.find_element(By.XPATH, '//option[. = "{playlist}"]'.format(playlist=playlist["Name"])).click()
            time.sleep(3)

            # 13. click the “Timed Broadcast” button
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(2) .my-auto:nth-child(2)"))).click()

            # 14. wait for the broadcast to finish
            time.sleep(int(playlist["Seconds"]))

            # 15. click the “Stop” button
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-secondary > .d-flex > .my-auto:nth-child(2)"))).click()

        # 16. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 17. click the “Homeopathics” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex:nth-child(4) > .btn > span"))).click()

        # 18. click the “By Symptoms” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lblBySymptomHomeopathics > span"))).click()

        # 19. for each loop of homeopathics
        for homeopathic in client["Homeppathics"]:

            print(homeopathic)
            print(homeopathic["Name"])

            # 20. click the dropdown box
            wait.until(EC.element_to_be_clickable((By.ID, "selHomeopathicsBySymptomsSelect"))).click()
            dropdown = wait.until(EC.element_to_be_clickable((By.ID, "selHomeopathicsBySymptomsSelect")))
            time.sleep(1)

            # 21. select the homeopathic
            dropdown.find_element(By.XPATH, '//option[. = "{homeopathic}"]'.format(homeopathic=homeopathic["Name"])).click()
            time.sleep(3)
            
            # 22. click the “Play” button
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mt-2 > .d-flex > .btn"))).click()

            # 23. wait for the broadcast to finish
            time.sleep(int(homeopathic["Seconds"]))

            # 24. click the “Stop” button
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex:nth-child(5) > .btn-secondary"))).click()

        # 25. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 26. click the “AOTune" then "Binaural Tones” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(1) > span"))).click()

        # 27. maybe click the "Gamma" button
        if client["AOTuneBinauralTones"]["Gamma"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 28. maybe click the "Schumann" button
        if client["AOTuneBinauralTones"]["Schumann"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 29. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 30. click the “AOTune" then "Planetary Frequencies” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(2) > span"))).click()

        # 31. maybe click the "Centering" button
        if client["AOTunePlanetaryFrequencies"]["Centering"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 32. maybe click the "Flower of Life" button
        if client["AOTunePlanetaryFrequencies"]["FlowerofLife_AlleviatePain_RelaxMuscles_Stress"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 33. maybe click the "Earth" button
        if client["AOTunePlanetaryFrequencies"]["Earth_Om_Relaxing_Soothing_Balancing"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 34. maybe click the "Pluto" button
        if client["AOTunePlanetaryFrequencies"]["Pluto_GroupDynamics"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 35. maybe click the "Mercury" button
        if client["AOTunePlanetaryFrequencies"]["Mercury_IntellectualCommunication"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(5) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 36. maybe click the "Mars" button
        if client["AOTunePlanetaryFrequencies"]["Mars_Focused Energy_StrengthOfWill"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(6) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 37. maybe click the "Saturn" button
        if client["AOTunePlanetaryFrequencies"]["Saturn_BecomingAware_Concentration"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(7) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 38. maybe click the "Geomagnetic Field" button
        if client["AOTunePlanetaryFrequencies"]["GeomagneticField_ImmuneSupport"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(8) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 39. maybe click the "Hydrogen Gamma" button
        if client["AOTunePlanetaryFrequencies"]["HydrogenGamma_Memory_Attention_Awareness"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(9) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 40. maybe click the "Earth Platonic Year" button
        if client["AOTunePlanetaryFrequencies"]["Earth_PlatonicYear_ClarityOfSpirit_Cheerfulness"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(10) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 41. maybe click the "Chiron" button
        if client["AOTunePlanetaryFrequencies"]["Chiron_Strength_Compassion_Wisdom"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(11) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 42. maybe click the "Sedna" button
        if client["AOTunePlanetaryFrequencies"]["Sedna_ATPProduction_Oxygenation"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(12) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 43. maybe click the "Jupiter" button
        if client["AOTunePlanetaryFrequencies"]["Jupiter_CreativePower"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(13) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 44. maybe click the "Culmination Cycle" button
        if client["AOTunePlanetaryFrequencies"]["CulminationCycle_ReduceAnxiety_Grounding"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(14) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 45. maybe click the "Earth Synodic Day" button
        if client["AOTunePlanetaryFrequencies"]["EarthSynodicDay_Dynamic_Vitalizing"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(15) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 46. maybe click the "Earth Sidereal Day" button
        if client["AOTunePlanetaryFrequencies"]["EarthSiderealDay_ImproveNervousSystem"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(16) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 47. maybe click the "Uranus" button
        if client["AOTunePlanetaryFrequencies"]["Uranus_Surprise_Renewal"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(17) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 48. maybe click the "Moon Synodic" button
        if client["AOTunePlanetaryFrequencies"]["MoonSynodic_SexualEnergyandCommunication"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(18) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 49. maybe click the "Neptune" button
        if client["AOTunePlanetaryFrequencies"]["Neptune_Intuition_DreamExperience"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(19) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 50. maybe click the "Venus" button
        if client["AOTunePlanetaryFrequencies"]["Venus_SkinandHairRejuvenation"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(20) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 51. maybe click the "Moon Sidereal" button
        if client["AOTunePlanetaryFrequencies"]["MoonSidereal_ImprovesSexualEnergy"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(21) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 52. maybe click the "Metonic Cycle" button
        if client["AOTunePlanetaryFrequencies"]["MetonicCycle_ImprovesReproductiveFunction"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(22) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 53. maybe click the "Moon Knot" button
        if client["AOTunePlanetaryFrequencies"]["MoonKnot_MaintainsEmotionalBalance"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(23) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 54. maybe click the "Saros Period" button
        if client["AOTunePlanetaryFrequencies"]["SarosPeriod_ImprovesReproductiveFunction"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(24) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 55. maybe click the "Apsidis Rotation" button
        if client["AOTunePlanetaryFrequencies"]["ApsidisRotation_Focus_Meditation_Prayer"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(25) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 56. maybe click the "Schumann Resonance" button
        if client["AOTunePlanetaryFrequencies"]["SchumannResonance_EnhancedLearning_Memory"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(26) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 57. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 58. click the “AOTune" then "Planetary Chakra Frequencies” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(3) > span"))).click()

        # 59. maybe click the "Solar Plexus" button
        if client["AOTunePlanetaryChakraFrequencies"]["SolarPlexus,_Power_Sun"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 60. maybe click the "Heart" button
        if client["AOTunePlanetaryChakraFrequencies"]["Heart_Earth_Om_Love"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 61. maybe click the "Throat" button
        if client["AOTunePlanetaryChakraFrequencies"]["Throat_Mercury_Communication"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 62. maybe click the "Crown" button
        if client["AOTunePlanetaryChakraFrequencies"]["Crown_EarthPlatonicYear_Spirituality"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 63. maybe click the "Root" button
        if client["AOTunePlanetaryChakraFrequencies"]["Root_EarthSynodicDay_Survival"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(5) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 64. maybe click the "Sacral" button
        if client["AOTunePlanetaryChakraFrequencies"]["Sacral_MoonSynodic_Sexuality"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(6) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 65. maybe click the "Third Eye" button
        if client["AOTunePlanetaryChakraFrequencies"]["ThirdEye_Venus_Intuition"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(7) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 66. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 67. click the “AOTune" then "Solfeggio Chakra Frequencies” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(4) > span"))).click()

        # 68. maybe click the "Crown" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Crown_TI_Spirituality"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 69. maybe click the "Third Eye" button
        if client["AOTuneSolfeggioChakraFrequencies"]["ThirdEye_SOL_Expression"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 70. maybe click the "Throat" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Throat_FA_Relationships"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 71. maybe click the "Heart" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Heart_MI_DNARepair"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 72. maybe click the "Solar Plexus" button
        if client["AOTuneSolfeggioChakraFrequencies"]["SolarPlexus_RE_UndoingSituationsandFacilitatingChange"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(5) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 73. maybe click the "Sacral" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Sacral_UT_LiberatingGuiltandFear"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(6) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 74. maybe click the "Root" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Root_VI_Energy_Rejuvenation"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(7) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 75. maybe click the "Sky" button
        if client["AOTuneSolfeggioChakraFrequencies"]["Sky_EA_ReducePain_AlleviateStress"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(8) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 76. maybe click the "Note C" button
        if client["AOTuneSolfeggioChakraFrequencies"]["NoteC_DO_Centering"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(9) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 77. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 78. click the “AOTune" then "Organs” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(5) > span"))).click()

        # 79. maybe click the "Adrenals" button
        if client["AOTuneOrgans"]["Adrenals"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 80. maybe click the "Bladder" button
        if client["AOTuneOrgans"]["Bladder"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 81. maybe click the "Blood" button
        if client["AOTuneOrgans"]["Blood"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 82. maybe click the "Brain" button
        if client["AOTuneOrgans"]["Brain"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 83. maybe click the "Colon" button
        if client["AOTuneOrgans"]["Colon"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(5) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 84. maybe click the "Fat Cells" button
        if client["AOTuneOrgans"]["FatCells"]:

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(6) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 85. maybe click the "Gall Bladder" button
        if client["AOTuneOrgans"]["GallBladder"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(7) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 86. maybe click the "Heart" button
        if client["AOTuneOrgans"]["Heart"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(8) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 87. maybe click the "Intestines" button
        if client["AOTuneOrgans"]["Intestines"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(9) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 88. maybe click the "Kidneys" button
        if client["AOTuneOrgans"]["Kidneys"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(10) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 89. maybe click the "Liver" button
        if client["AOTuneOrgans"]["Liver"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(11) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 90. maybe click the "Lungs" button
        if client["AOTuneOrgans"]["Lungs"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(12) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 91. maybe click the "Muscles" button
        if client["AOTuneOrgans"]["MuscleCells"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(13) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 91. maybe click the "Pancreas" button
        if client["AOTuneOrgans"]["Pancreas"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(14) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 94. maybe click the "Stomach" button
        if client["AOTuneOrgans"]["Stomach"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(15) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 95. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 96. click the “AOTune" then "DNA and RNA” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(6) > span"))).click()

        # 97. maybe click the "DNA Guanine" button
        if client["AOTuneDNAandRNA"]["DNA_Guanine"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 98. maybe click the "DNA Cytosine" button
        if client["AOTuneDNAandRNA"]["DNA_Cytosine"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 99. maybe click the "RNA Thymine" button
        if client["AOTuneDNAandRNA"]["RNA_Thymine"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 100. maybe click the "DNA Adenine" button
        if client["AOTuneDNAandRNA"]["DNA_Adenine"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 101. maybe click the "RNA Phenylalanine" button
        if client["AOTuneDNAandRNA"]["RNA_Phenylalanine"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(5) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 102. maybe click the "RNA Adenine" button
        if client["AOTuneDNAandRNA"]["RNA_Uracil"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(6) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 103. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 104. click the “AOTune" then "Spiritual Insights” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(7) > span"))).click()

        # 105. maybe click the "Pineal Gland" button
        if client["AOTuneSpiritualInsights"]["PinealGland"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 106. maybe click the "Spiritual Awakening 1" button
        if client["AOTuneSpiritualInsights"]["SpiritualAwakening1"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 107. maybe click the "Spiritual Awakening 2" button
        if client["AOTuneSpiritualInsights"]["SpiritualAwakening2"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 108. maybe click the "Spiritual Awakening 3" button
        if client["AOTuneSpiritualInsights"]["SpiritualAwakening3"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 109. go to sefi page
        driver.get("https://app.aoscan.com/sefi")

        # 110. click the “AOTune" then "Otto Clearning and Connecting” button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(8)"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex > .btn:nth-child(8) > span"))).click()

        # 111. maybe click the "OTTO Clearing and Connecting 1" button
        if client["AOTuneOttoClearningandConnecting"]["OTTOClearingandConnecting1"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(1) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 112. maybe click the "OTTO Clearing and Connecting 2" button
        if client["AOTuneOttoClearningandConnecting"]["OTTOClearingandConnecting2"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(2) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

        # 113. maybe click the "OTTO Clearing and Connecting 3" button
        if client["AOTuneOttoClearningandConnecting"]["OTTOClearingandConnecting3"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(3) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)
        
        # 114. maybe click the "OTTO Clearing and Connecting 4" button
        if client["AOTuneOttoClearningandConnecting"]["OTTOClearingandConnecting4"]:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-group-item:nth-child(4) > .flex-grow-1"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-center:nth-child(1)"))).click()
            time.sleep(120)

finally:
    input("Press Enter to close…")
    driver.quit()
