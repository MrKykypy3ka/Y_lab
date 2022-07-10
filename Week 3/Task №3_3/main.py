from savetheplace import SavePlace
from heroes import Superman, ChuckNorris
from places import Kostroma, Tokyo, Krypton
from massmedia import Tv


if __name__ == '__main__':
    SavePlace(Superman(), Kostroma(), Tv('RTR'))
    print('-' * 20)
    SavePlace(ChuckNorris(), Tokyo(), Tv('RenTv'))
    print('-' * 20)
    SavePlace(Superman(), Krypton(), Tv('UFOtv'))
