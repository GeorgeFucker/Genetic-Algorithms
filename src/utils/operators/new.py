class Operator:

    @staticmethod
    def segregate():
        """
            Selects randomly parts of random length from genes.
            
            args:[bool] - list of genes.
        """

        def func(*args):
            args = list(args[:])
            gene_length = len(args[0])
            points = sorted(np.random.choice(range(1, gene_length - 1), len(args) - 1, replace=False))
            np.random.shuffle(args)
            print(points)
            idx = np.random.randint(gene_length - points[0])
            offspring = args[0][idx: idx + points[0]]
            for i in range(len(points) - 1):
                length = points[i + 1] - points[i]
                idx = np.random.randint(gene_length - length)
                offspring += args[i + 1][idx: idx + length]
            idx = np.random.randint(gene_length - points[-1])
            offspring += args[-1][idx: idx + (gene_length - points[-1])]

            return [offspring]

        return func

    @staticmethod
    def dublicate(length):
        """
            Selects randomly part of gene with some length and replace another part.
            
            gene:[bool] - gene.
            length:[int] - length of the gene.
        """

        def func(gene):
            old_idx = np.random.randint(len(gene) - length + 1)
            available_indices = set(range(len(gene) - length))
            available_indices -= set(range(old_idx - length + 1, old_idx + 1))
            available_indices -= set(range(old_idx, old_idx + length))
            new_idx = np.random.choice(list(available_indices))

            gene[new_idx: new_idx + length] = gene[old_idx: old_idx + length]

            return [gene]

        return func
