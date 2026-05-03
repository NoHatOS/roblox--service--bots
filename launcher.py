import requests
import time
import webbrowser

# --- CONFIGURACIÓN DEL ESCUADRÓN ---
# ID que me pasaste: 96315161399686
PLACE_ID = "96315161399686" 

COOKIES = [
    "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhwKBGR1aWQSFDE4NDI3NDQ2OTY0MDA2NjYyNzM0KAM.MlEqcgyimKFRxCP_88vWvWmAAh5mg9_oummIkPICXSYLaza80rorCR-zvXSoIqSZA6o6r5-5ulIsBCnhOpmzPWK_fzKzcN_YIOX6NPQMupsNLJBT46rj2BIbcvV3qgBQjO7aAK5zdbgsJ1kmbu8u8oOArEohVemeHs0KtctRTgwE-LysIP5FomZrQhqkEdLlwzsTjeATsYyUK7rcAaaHrCQxb44GCf2iIcX5RsdAjzJSTDKR_HOqv77Dd9sWE-mJm38bI9ee5nKTp1wryd7-VD0nGe_-Da8Vy8XPuJZaLS_LY0QTkNjCF6ZyoBib-xJJMdvxGF_F4HmKDreYmc-N0Q2eODd9z5ni3ARvi_w-XwEyP2RrPqmd2n9_jWJsGscorMzOFK3FhwVDKwUvgZ4IspZtMDwOcwLeTdg0kOfj8D8i-mUhAT8AkCtO7tzGon4-CqhnQzg7t5PjScWyYuTU6TPL5Br9jEqEPYSPP03RiPuezQ6mZJDBZ4L59TIyc1vQNAW4Mt9HGn9a620N_Bnahp85kvI3_ZAVj_f8vc2Ji84CQn2RDcwNN7uWnHKV8L3lw9YcglDw2hkzfO1nzJHyLTs4vLOpOV-dZD0K3E28jBnullGB5LYU1oxTEjZvskY6pmhz9OCOm07ffmDs44FpXEY1Mh8XLHsKirw_mPTCsa3FMNRBiPZnv1lGjd-JkcNT4ElTo9eviiMENqP5otGUKuIwUN2kSyvYveGkwmfMbZ8dAuqPribuY4Glv-X7yhF0_I2uMT4gAFthlBZa3ZPOkx3m2uR2p8WOe8aphfbsjB4qRcmTOEM6Emsg3yaYHCR3GodHK73Ps-N_EibXnb3wRZLo8s7tHX_WXlDG31RFexTdSC9AkdfbagGywCDS7Zkmy6so69RVZkvUOEEzkJfuV-ky0vula2bxMMnIXbFjZ4umkiJ2i6umWKhevdSiznxlSPPQYw",
    "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhwKBGR1aWQSFDEwMDQ3OTA5NjgyOTU5MjQ4NzQ1KAM.pr2fPzCQqQ4PPbpoSfvGgVC9p5WFQolLdliOm7MQSx3WbF0ovIoc_dLNKan4qDMxD0RjUg9qrVyr5XnYyU3Kw67VR8m8vQXXcSJwt7gGGO4XKb1bvYGqW_uXRAcyF5_01QYQl2ur865ZuJAPQUNCyNwOqcyuuxruI_oCgzsVQQ5yrzM29wghP_7Yf7oEyKE6wH7gwuki5vGAg95zpskE9sGwdKDWIwe5dswUZsAtSAnO7w-mMH-et0WAgojDzjnx6uql8cAXBsffADDRV3K0v5_jN2RgquBeJULT76dejbBrmO4FvyMsD2XlVA9B2lMVnKGTH9fVjX2Yn0J9KMDi0DAmlvNKPsfYmvYhvMy-0X_3SPVn1RiQcjE9GXAIJqOcvdzdxTL-Yc3NxugoGrfEyY0Z3MBDCxHrO6yMvGvLExS51gCZ9OlpV94DO8AyP-DQJ3O6B-E8_BDbwhjEi4dxt5gIwPF-Gs7EPnwEG_p2FSyLT6QVmwRycomM_Mmjkez5H9sdcXtR3VUHH2jwvwAimfNRJ-kHonFIzSwUwk4I_9WY7s42YLJFfb0GLJ6jPDwlpH-lnelzhvtLarafE3YhAfxpCRRWQzRFq0p1oDx8gSVn3Q1Cnlez5WU6WRDxg1Eu0JVEQzWLvWzMNV_gLSoVme_21ODvFuumuXZcaIu0ejqGmeoPOtk6j3LwGu4T32HB0NwHIZpRF5OHSqq0AsqvueMGMXlJkGASv6SvBvBYrMxeBi0nLnvFcR9icreGmUnfVeVpvB_4iGMEpGie979gp7b8kbwTthfCTKHY45mrM16QtWR8fzIVW5MsXrwvMEgBNFPFasyzdBQhMFlYVFW4ApRDClhNowWJTPBxwJWItInW1ouDOLyIMH-2Vv58bduPl2-9J7FMVZjsXzOc10o9ZP_MWKZ4vLfPUEauahnSM3N7oqkQra94BdxYufPeBEJLjPg2YKq_MrIVqYihOtH8rSRrS_g",
    "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhsKBGR1aWQSEzUyODM2NzMxMjQ4NzQ1MDQ1NDkoAw.pKddZD429HHC1xxOOZtT0vMXVRALSDcLKz9NR8Cnf72aeHZ1bPDacH1xVUJbzHW-FY7gIENQaD4kSMIliA729M_Iqznz-i2rWw8m3smuon5TgzdRXQc0ycfJcLZIBxOuhXYSwg_qhZKuJsF-D52bhFcozygMdcEkLBOGdkdh03tCf6aaBH9j-lqrc77wQ1vB82zK3q-7xlT2wfrC3w62qiFDFbPF2rfDw1-ze5ttNrJXU7XCNozgAWsOrT_KmlJQG01zAk9aWKDSQOd-mwB_O6vQEI6sSp2VLxWat1aKUwA-VP0nrIztSdsfepf3dKRNExtR57jyT3DbThbGGwhQeX84OwAXZFuL-PzGXXrEkE_JQ1w_2gjuGQYGG8aZfrZv6nKofHuEDM6GCZa99CZ7MonnTjKSaK0_AoLs1WOZ2pbktcAGhrCtiqKJ36OSznHl68FFID0ROhg8TXM5aCMgfgKEX8V9LPfn-QWzWyo9euTobNfRQHgu_gKT2MOkQ4VPJT5QPnYNGD_dRwdVSfpcNcb4f8YfCs7BVdbPeTgyBA-72SemScs3blfe5mKSLf3WvWcxCJN2XnFZQvNvjFee17B91Rww9rS3sOGQedbh9Lhcpgexvvi3T898GfQrVVCb78ZY8FZK6NSIUp3G25leqhBmo9uc8R1cA2T3yYssi96LpNfqtBtyNauAOk_fK5YbO1hu-oRrM4MNNPHJ4u2mlh1_FkUrBMLUox3y7PN9r4bMKA4GyPcZ9YrRJgGbYRdJaIy6rjxRblU5GAT-VnNDr6l90Gl4X0q8FZifiHpw03Ys4M9txofpAUI87EbDdQJupiZSA4NyvpVn3kiNf9D1b1zeXt5728ujVRvA2EW1WkWl568_4am9GJpjOFMMphcn7aoSmdNaTzWdoWVXInc6BcRlhgD8eJ0T_T9GaDoQztJEosj5VsMZ5mVqLOK2tE3sANI3zlJ0Mor6YiciBEhbYchaasw",
    "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhsKBGR1aWQSEzYzNDk1MzAyNjk1ODEyNzA0MTkoAw._vnPYf6hdWCOnlV5DGpGImWqjnayU0FkrddLN16BuUSNu1jNd9_tcj7vyxQfQ7E7mLgPjp2w-9VnWVgRjDyae9IVCx_xMsdZsLYDF-jK1SkRasZQDjTfh5Vgf5Bz9WNkIbzXfJIU6Y2a0qIsF0BzdZptsb11ikEkoZfWkV2ieJ_ew8z2r1kO1jq7p5N4YzkNfnYEcBMqNWuBXDPbYSud2y_wKuPN3O89d9v8Kw951ulqCSpi-VQhaLQvDgCoyZAfrRZhphTu8ZVKpWjhuTDeBHIWraHoY4RrbC-xF0WlQBpU_ZIJGl0Jo63AFgXHofd3P3KN5OQ-xxAnKCMH5o5dSyaU1qqW9-esLqfE2Zr7G_upQwWruxpfHwGQJZn2ieWAgOhNXup-j3_naYiZYeD_hqHpLM2dkG9QjxKFp8ezuqa0zg_Qo4h-xPtfQRdxmioANtx_Sp2YS1zBMikzq6QsLqsAivCGbFf0q5vxuazyzUrvoPeKXV_s9BukGnfVcVhXcBTgBl-9n7GT2QD2cZ6NVJshYNqkjnKzF0IzLVna31hM4eTq21v6-3hPch4cngsgNeNynw5-002TJuGFrkvATf6eKpG9pv8eBP3h8pNb2rBgK3lfdIHsr1YgDc2oTtCyeL4xvzfeV7tpN5bjdNENUvdaLHntwl1YWwi040rOR0e5VrTwD0NPFjqvoCbgrwwmVx8Cm7zVCeRZCWQlNxE0ZsZ2Re-uyzeTxn1jWIzE6MZi66SZHwdfSMICrhUPegLKu4WjNT4fBeFFw5x9Xzpu43UsK8qKG7yxGmPcxSA8boWcFD0aTlAeFXbGUCzS7KOsb41uZt6EAjfbzHlG5WE_Bcsz-Uc3Mrq1GrmGET60bWOKxr_RHHIxTh6bDh_orTWsqa-JOL8m468vqWwxMGuEf7NHOB7a3e-zcX1sPRrmvW9eran9fnrmMmw7bL_xVxdSVf_PqPIn03BjEyAMoJ1QkvVjy-o",
    "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhADIhsKBGR1aWQSEzk5MDI0NTA3MTcyMzA1MDQ2ODgoAw.ne-N9DLJvv0xObtGWUMpRvPQx7At34m9o_kac-uYe5_84mTxEqjVJD8QG_aUy8SEIrZvi5CGkQW9Qw4V9HHfrijp-4-l7gPBp_HtGlh6-7nSFpVGscVNVCbaXV21i2vSaNxGlvepnkp54J0XjwYW_TMdsPJuHnjKzd9oCn0AM3W3bmHiisn6FPpaMMsFmxWfUdl4PpCXiVJdgNh5KWzFEZQhuUqjyoh4jdvlhOv6EhH7WmZPdHEfeZl_9LrvUvPwvJ-Lcy1HrNhodJLVn_dzc4EGBaDeox2BlAXb1W0VzVdTWbs8WZz231I6Cf3oBI-qtmGWNxzWhZD9tqlsFF4N9z7cuAtqTWBwn9c4Q0sRzYQUnN-W4hvzFubE1-vpcymZE8bK86rF_YrtCQfPFwvzEV2ofdJO2B4SK9eJUtsehvhoysWbREDe36ZPo2TKvEZDRohLIrjabjUxY5qMQ_IJvsfQ0TrqBZ8Yw1V-tTOikTdtc6WowDHiCElAtf7KBfpkFSKq1pSEgVEsqqvXQXeqxaj3PwHvOkcKuUuwM-aUPwgoISH2uPUxSAxq-wJ6y7FgBw1CyEtzTVNZ57mOqVNqYOyMMbvqalbGtmsLZq8cbUcOtMaf-JCLVKItp4nclsBQ-8bD7L8xidOuOMRH_ruqT6fB_UPKdK7Klc7lSrbvfLXJrWh1e8-vSN8WqpS5aydj63ij6Rd6h2oMEwnELmjdrzosX7PoHm6nicUMlZkS3OvRsxFzp4VeCEeSk83KWrHT-k2EkGGYUSf3b4BkFa8mqHsNz7ownB-POt6MZ3GiaJLnf_YFObB_2x0m6VYV5JIhJHnDi0RmEAFT8hvzncoPypJJNG3cb9CWsqGdafcyfSmaUh4uc4z3UKCKo0cmyVv1bNnzKbt1xOyocmv6HWSk6IV_aCpXuOQRzP7VRt7Pf5sHcbGR4UbQgo55TH0oGpEyqKfwAQ"
]

def desplegar_escuadron():
    print("--- DESPLEGANDO ESCUADRÓN SERVICE ---")
    for i, cookie in enumerate(COOKIES, 1):
        print(f"[*] Lanzando Bot #{i}...")
        try:
            # Solicitud del ticket de autenticación
            r = requests.post(
                "https://auth.roblox.com/v1/authentication-ticket",
                headers={"Cookie": f".ROBLOSECURITY={cookie}", "Referer": "https://www.roblox.com/"}
            )
            ticket = r.headers.get("rbx-authentication-ticket")
            
            if ticket:
                # Abrir Roblox con el ID de juego proporcionado
                webbrowser.open(f"roblox://placeID={PLACE_ID}&testMode=false&authTicket={ticket}")
                print(f"[OK] Bot #{i} en camino.")
            else:
                print(f"[ERROR] Bot #{i}: No se pudo obtener el ticket.")
        except Exception as e:
            print(f"[ERROR] Bot #{i}: {e}")
        
        # Pausa de 12 segundos entre bots para estabilidad
        time.sleep(12)

if __name__ == "__main__":
    desplegar_escuadron()
