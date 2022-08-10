__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = seconds/86400
    seconds = seconds % 86400
    days = int(days)
    hours = seconds/3600
    seconds = seconds%3600
    minutes = seconds/60
    seconds = seconds%60
    result=''
    hours = int(hours)
    minutes = int(minutes)
    print(minutes,hours)
    if(days != 0):
        if(days<10):
            result += f'0{days}d'
        else:
            result += f'{days}d'
    if(hours != 0 or days > 0):
        if(hours<10):
            result += f'0{int(hours)}h'
        else:
            result += f'{int(hours)}h'
    if(minutes != 0 or days > 0):
        if(minutes<10):
            result += f'0{int(minutes)}m'
        else:
            result += f'{int(minutes)}m'
    if(seconds<10):
        result += f'0{int(seconds)}s'
    else:
        result += f'{int(seconds)}s'

    return result




