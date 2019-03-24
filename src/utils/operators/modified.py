import numpy as np

from itertools import permutations, chain

class Operator:
    class Mutate:
        """
            Mutation operators.
        """

        @staticmethod
        def multi(positions=2):
            """
                Changes gene in several positions.

                gene:[bool] - list of genes.
                positions:int - number of positions.
            """

            def mutate(gene):

                indices = np.random.choice(range(len(gene)), positions, replace=False)

                for idx in indices:
                    gene[idx] = not gene[idx]

                return gene

            return mutate

        # @staticmethod
        # def selective(positions=2):
        #     """
        #         Creates offspirngs mutated at random positions.
        #         Then chooses one which is the best.
        #
        #         gene:[bool] - list of genes.
        #         positions:int - number of offsprings.
        #     """
        #
        #     def mutate(gene):
        #
        #         indices = np.random.choice(range(len(gene)), positions, replace=False)
        #
        #         offsprings = []
        #         for idx in indices:
        #             offspring = gene[:]
        #             offspring[idx] = not offspring[idx]
        #             offsprings.append(offspring)
        #
        #         return offsprings
        #
        #     return mutate

    class Inverse:
        """
            Inverse operators.
        """

        @staticmethod
        def multi(positions=2):
            """
                Divides gene at several points and then change them randomly.
                
                gene:[bool] - list of genes.
                positions:int - number of parts.
            """

            def inverse(gene):
                indices = np.random.choice(range(len(gene)), positions, replace=False)

                slices = [slice(0, indices[0])]
                for i in range(len(indices) - 1):
                    slices.append(slice(indices[i], indices[i + 1]))
                slices.append(slice(indices[-1], None))
                np.random.shuffle(slices)

                offspring = []
                for part in slices:
                    offspring += gene[part]

                return offspring

            return inverse

        # @staticmethod
        # def selective(positions=2):
        #     """
        #         Sequential applying of basic inverse operator at different positions.
        #         Then choose the best offspring.
        #
        #         func:function - fitness function.
        #         gene:[bool] - list of genes.
        #         positions:int - number of offsprings.
        #         type_:str - type of gene representation.
        #     """
        #
        #     def inverse(gene):
        #         indices = np.random.choice(range(len(gene)), positions, replace=False)
        #
        #         offsprings = []
        #         for idx in indices:
        #             offspring = gene[idx:] + gene[:idx]
        #             offsprings.append(offspring)
        #
        #         return offsprings
        #
        #     return inverse

        @staticmethod
        def fragmentive(fragments=2, length=2):
            """
                Selects several unintersected fragments and change their order randomly.
            
                gene:[bool] - list of genes.
                fragments:int - number of fragments.
                length:int - length of each fragment.
            """

            def inverse(gene):
                assert len(gene) >= length * fragments

                fragments_list = [[gene[i + j] for j in range(length)] for i in range(len(gene) - length + 1)]

                available_indices = set(range(len(fragments_list)))

                generated_fragments_indices = []
                while len(generated_fragments_indices) < fragments:
                    idx = np.random.choice(list(available_indices))
                    generated_fragments_indices.append(idx)
                    available_indices -= set(range(idx - length + 1, idx + length))

                ordered_indices = generated_fragments_indices[:]
                ordered_indices = sorted(ordered_indices)
                np.random.shuffle(generated_fragments_indices)

                for old_idx, new_idx in zip(ordered_indices, generated_fragments_indices):
                    gene[old_idx:old_idx + length], gene[new_idx:new_idx + length] = gene[
                                                                                     new_idx:new_idx + length], \
                                                                                     gene[old_idx:old_idx + length]

                return gene

            return inverse

    class Crossover:
        """
            Crossover operations.
        """

        # @staticmethod
        # def multi_chromosomal():
        #     """
        #         It is modified crossover operator which takes more than 2 parents and diving gene by (P - 1)
        #         parts creates offspings. P - amount of parents.
        #
        #         args:[[bool]] - list of parents' genes.
        #
        #     """
        #
        #     def crossover(*args):
        #         parents_amount = len(args)
        #         gene_length = len(args[0])
        #         assert gene_length >= parents_amount
        #
        #         points = np.random.choice(range(gene_length), parents_amount - 1, replace=False)
        #         points = sorted(points)
        #
        #         slices = [slice(None, points[0])]
        #         slices.extend([slice(points[i], points[i + 1]) for i in range(len(points) - 1)])
        #         slices.append(slice(points[-1], None))
        #
        #         offsprings = []
        #         parents_order = permutations(args)
        #
        #         for parents in parents_order:
        #             offspring = [parents[i][slices[i]] for i in range(parents_amount)]
        #             offspring = list(chain(*offspring))
        #             offsprings.append(offspring)
        #
        #         return [offsprings]
        #
        #     return crossover

        @staticmethod
        def multi_positional(positions=2):
            """
                Crossbreeds two gene at different position resulting with two offsprings.
                          
                gene_a:[bool] - gene a.
                gene_b:[bool] - gene b.
                positions:int - number of crossbreeding positions.
            """

            def crossover(*args):
                assert len(args) == 2, 'There must be only 2 parents'
                gene_a, gene_b = args

                points = sorted(np.random.choice(range(1, len(gene_a) - 1), positions, replace=False))

                offspring_a = gene_a[:points[0]]
                offspring_b = gene_b[:points[0]]

                for i in range(positions - 1):
                    if i % 2 == 0:
                        offspring_a += gene_b[points[i]:points[i + 1]]
                        offspring_b += gene_a[points[i]:points[i + 1]]
                    else:
                        offspring_a += gene_a[points[i]:points[i + 1]]
                        offspring_b += gene_b[points[i]:points[i + 1]]

                if positions % 2 == 0:
                    offspring_a += gene_a[points[-1]:]
                    offspring_b += gene_b[points[-1]:]
                else:
                    offspring_a += gene_b[points[-1]:]
                    offspring_b += gene_a[points[-1]:]

                return [offspring_a, offspring_b]

            return crossover

        @staticmethod
        def homogeneous(threshold=0.5):
            """
                Makes offspring using threshold. If random number >= threshold then gene_a[0] is taken.
              
                gene_a:[bool] - gene a.
                gene_b:[bool] - gene b.
                threshold:[float] - threshold. 0 < threshold < 1
            """

            assert 0 < threshold < 1

            def crossover(*args):
                assert len(args) == 2, 'There must be only 2 parents'
                gene_a, gene_b = args

                offspring_a = []
                offspring_b = []

                for i in range(len(gene_a)):
                    if np.random.random() < threshold:
                        offspring_a.append(gene_a[i])
                        offspring_b.append(gene_b[i])
                    else:
                        offspring_a.append(gene_b[i])
                        offspring_b.append(gene_a[i])

                return [offspring_a, offspring_b]

            return crossover

        @staticmethod
        def templated(template=None):
            """
                Takes template as gene. If template[i] == 0 then gene_a.
                
                type_:str - type of gene representation.                
                gene_a:[bool] - gene a.
                gene_b:[bool] - gene b.
                template:[bool] - template. Using if we define offsprings.
            """

            def crossover(*args, template_=template):
                assert len(args) == 2, 'There must be only 2 parents'
                gene_a, gene_b = args

                if not template_:
                    template_ = np.random.randint(2, size=len(gene_a))

                offspring_a = []
                offspring_b = []

                for i in range(len(template_)):
                    if template_[i]:
                        offspring_a.append(gene_a[i])
                        offspring_b.append(gene_b[i])
                    else:
                        offspring_a.append(gene_b[i])
                        offspring_b.append(gene_a[i])

                return [offspring_a, offspring_b]

            return crossover
