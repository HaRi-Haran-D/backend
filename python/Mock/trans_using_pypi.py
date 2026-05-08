import asyncio
from googletrans import Translator

async def translate_text():
   async with Translator() as translator:
       result = await translator.translate('सुबह की ताज़ी हवा मन को शांति और ऊर्जा प्रदान करती है। '
                                           'पेड़-पौधे हमारे जीवन के लिए बहुत महत्वपूर्ण होते हैं क्योंकि वे हमें स्वच्छ हवा और छाया देते हैं। '
                                           'हमें हमेशा प्रकृति की रक्षा करनी चाहिए और पर्यावरण को स्वच्छ रखना चाहिए। स्वच्छ और हरा-भरा वातावरण जीवन को स्वस्थ, '
                                           'सुखमय और सुंदर बनाता है')
       print(result.text)

asyncio.run(translate_text())


