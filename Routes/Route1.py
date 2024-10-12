import logging
from aiogram.filters import CommandStart
from aiogram.types import Message, Document
from aiogram.dispatcher import router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import aiohttp
from bs4 import BeautifulSoup
from Texts import Router1

router = router.Router(name=__name__)


class StateRoute(StatesGroup):
    Greetings = State()
    YouTube = State()
    TikTok = State()
    Instagram = State()


@router.message(CommandStart())
async def starting(message: Message, state: FSMContext):
    await state.set_state(StateRoute.Greetings)
    await message.answer(Router1.Greetings)


async def downloadTiktok(url: str, method: int, state: FSMContext):
    await state.set_state(StateRoute.TikTok)
    header, cookies, params, data = None
    headersGlobal = {
        'Referer': 'https://ssstik.io/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    if method == 2:
        cookies = {
            'cf_clearance': 'zeYX3sNGqSB3NWaab6EDE8LNeVlvqU.vZWlyCiSuqGw-1728731314-1.2.1.1'
                            '-G5NfJDzhEVCy12ihfK8mDtXtWIGKebTN8qzLu6biGS4sIsP1AkCSQ6gs_fMQz'
                            'R6dcMDA_I3LU5MMhZmyz26TtufRDlx04Mj9eVOnlh79Kcgb_KMdIzkMiRLIowy'
                            'E18ldbpqwRsEjfpO0cPocCu6KvN5to36jZ2sn48fVo_fXBsf4BDkpm4yj.BBp6'
                            'TPCW.mJRHJ4PynzmUfYXd2llrOSI_RDsy2FqatHonCnOzBYHrA3GEuhOfNh3Ee'
                            '.oNY7ptWJlrjw5Ld7v8StTOY_8CQaEYtc0HAxi9eQRHjhoWzGpalJJrydeYFNh'
                            'nB9LmQoDuoVCpJeaYH5Ohke8tXJKmhc8Zd9qRUcFG1dbfTk_b6vyyGB9jj7Heb'
                            'eZaTqS_Q3OLdpDdzDejHS4c23HVGprZVjs7NOgIEYTQNXCKYxGGagPKP_oXtAX'
                            'X3O4BjdKYDMDf9zFCsIm4IlHJIOU7EEIszeuw',
            '_ga': 'GA1.1.2068031437.1728731319',
            '_ga_ZSF3D6YSLC': 'GS1.1.1728758514.4.1.1728758539.35.0.0',
        }
        headers = {
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'hx-current-url': 'https://ssstik.io/en-1',
            'hx-request': 'true',
            'hx-target': 'target',
            'hx-trigger': '_gcaptcha_pt',
            'origin': 'https://ssstik.io',
            'priority': 'u=1, i',
            'referer': 'https://ssstik.io/en-1',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"24.7.6.974"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.234", '
                                           '"YaBrowser";v="24.7.6.974", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
        }
        data = {'id': url,
                'locale': 'en',
                'tt': 'WjQxNHI0'
                }
        params = {'url': 'dl'}

    async with aiohttp.ClientSession('https://ssstik.io') as session:
        request = await session.post('/abc', params=params, data=data, headers=headers, cookies=cookies)
        logging.info('Подлючен к https://ssstik.io')

        soup = BeautifulSoup(await request.text(), 'html.parser')

        url = ((soup.find('div', id='dl_btns')).find('a'))['href']

    idvideo = url.split('/')[-1]

    async with aiohttp.ClientSession('https://tikcdn.io', headers=headers) as session:

        logging.info("Подлючен к https://tikcdn.io/")

        async with session.get(url=f'/ssstik/{idvideo}', headers=headers) as request:
            request.raise_for_status()

            with open(f'{idvideo}.mp4', 'wb') as video:
                logging.info("Начало загрузки видео")
                try:
                    video.write(await request.read())
                    logging.info("Видео успешно загружено")
                except Exception as e:
                    logging.error(e)

                return idvideo


async def downloadYoutube(url: str):
    ...


async def check_type_url(data: str, state: FSMContext):
    logging.basicConfig(filename="Log.log", level=logging.DEBUG, filemode='a', encoding='utf-8',
                        format="%(asctime)s : %(name)s - %(module)s.%(funcName)s : %(levelname)s ---- %(message)s")

    text = data.split('/')[2]
    Domens = {
        'm.youtube.com': lambda: ...,
        'youtu.be': lambda: ...,
        'youtube.com': lambda: ...,
        'www.tiktok.com': lambda url, state: downloadTiktok(url, 1, state),
        'vt.tiktok.com': lambda url, state: downloadTiktok(url, 2, state)
    }
    for domen in Domens:
        if text == domen:
            func = Domens[domen]
            return await func(data, state)


@router.message()
async def distribution(message: Message, state: FSMContext):
    if state.get_state() == StateRoute.Greetings:
        await check_type_url(message.text, state)
