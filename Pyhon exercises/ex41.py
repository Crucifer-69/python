#   * * * * * * * * * *
#   * * * *     * * * *
#   * * *         * * *
#   * *             * *
#   *                 *
#   *                 *
#   * *             * *
#   * * *         * * *
#   * * * *     * * * *
#   * * * * * * * * * *


for i in range(0, 5):
    print()
    for j in range(i, 5):
        print("*", end=' ')
    for j in range(0, i):
        print("   ", end=' ')
    for j in range(i, 5):
        print("*", end=' ')


for i in range(0, 6):
    for j in range(0, i):
        print("*", end=' ')
    for j in range(i, 5):
        print("   ", end=' ')
    for j in range(0, i):
        print("*", end=' ')
    print()
