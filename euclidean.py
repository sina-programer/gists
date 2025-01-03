import numpy as np

def euclidean(p1, p2):
    assert np.equal(np.shape(p1), np.shape(p2)), 'The points muse have the same dimensions'
    return np.sqrt(
        np.sum(
            np.fromiter(
                (
                    np.power(
                        np.subtract(
                            p1[i],
                            p2[i]
                        ),
                        2
                    )
                    for i in np.arange(np.shape(p1)[0])
                ),
                np.float64
            )
        )
    )


if __name__ == "__main__":
    assert euclidean([0, 0], [1, 1]) == np.sqrt(2)
    assert euclidean([1, 0], [0, 0]) == 1
    assert euclidean([0, 0], [0, 2]) == 2
    assert euclidean([0], [5]) == 5
    assert euclidean([0, 1, 0], [0, 0, 0]) == 1
    assert euclidean([0, 0, 0, 0], [1, 1, 1, 1]) == 2
    assert euclidean([-1, -1], [1, 1]) == 2*np.sqrt(2)
    assert euclidean([0, 0], [3, 4]) == 5
    print('All tests passed!')
