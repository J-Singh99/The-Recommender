# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:22:34 2018

@author: Frank
"""
from EvaluationData import EvaluationData
from EvaluatedAlgorithm import EvaluatedAlgorithm
import joblib
class Evaluator:
    
    algorithms = []
    
    def __init__(self, dataset, rankings, movies):
        ed = EvaluationData(dataset, rankings, movies)
        self.dataset = ed

    def AddAlgorithm(self, algorithm, name):
        alg = EvaluatedAlgorithm(algorithm, name, self.dataset)
        self.algorithms.append(alg)
        
    def Evaluate(self, doTopN):
        results = {}
        for algorithm in self.algorithms:
            print("Evaluating ", algorithm.GetName(), "...")
            results[algorithm.GetName()] = algorithm.Evaluate(self.dataset, doTopN)

        # Print results
        print("\n")
        
        if (doTopN):
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                    "Algorithm", "RMSE", "MAE", "HR", "cHR", "ARHR", "Coverage", "Diversity", "Novelty"))
            for (name, metrics) in results.items():
                print("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(
                        name, metrics["RMSE"], metrics["MAE"], metrics["HR"], metrics["cHR"], metrics["ARHR"],
                                      metrics["Coverage"], metrics["Diversity"], metrics["Novelty"]))
        else:
            print("{:<10} {:<10} {:<10}".format("Algorithm", "RMSE", "MAE"))
            for (name, metrics) in results.items():
                print("{:<10} {:<10.4f} {:<10.4f}".format(name, metrics["RMSE"], metrics["MAE"]))
                
        print("\nLegend:\n")
        print("RMSE:      Root Mean Squared Error. Lower values mean better accuracy.")
        print("MAE:       Mean Absolute Error. Lower values mean better accuracy.")
        if (doTopN):
            print("HR:        Hit Rate; how often we are able to recommend a left-out rating. Higher is better.")
            print("cHR:       Cumulative Hit Rate; hit rate, confined to ratings above a certain threshold. Higher is better.")
            print("ARHR:      Average Reciprocal Hit Rank - Hit rate that takes the ranking into account. Higher is better." )
            print("Coverage:  Ratio of users for whom recommendations above a certain threshold exist. Higher is better.")
            print("Diversity: 1-S, where S is the average similarity score between every possible pair of recommendations")
            print("           for a given user. Higher means more diverse.")
            print("Novelty:   Average popularity rank of recommended items. Higher means more novel.")
        
    def SampleTopNRecs(self, ml, filename="all", testSubject=85, k=10):
        
        for algo in self.algorithms:
            print("\nUsing recommender ", algo.GetName())
            
            print("\nBuilding recommendation model...")
            trainSet = self.dataset.GetFullTrainSet()
            algo.GetAlgorithm().fit(trainSet)

            joblib.dump(algo, filename)

            print("Computing recommendations...")
            user_items = {3601, 20, 27, 3612, 30, 31, 32, 34, 35, 36, 2085, 2090, 42, 43, 48, 49, 2100, 52, 54, 55, 56, 57, 58, 59, 60, 61, 64, 66, 67, 68, 69, 72, 2121, 73, 75, 76, 79, 83, 86, 87, 88, 89, 90, 91, 92, 93, 2144, 97, 99, 100, 101, 4205, 4206, 4207, 4208, 4209, 4210, 4211, 650, 651, 142, 656, 145, 146, 659, 148, 151, 154, 156, 670, 674, 675, 680, 683, 684, 690, 2234, 2236, 701, 702, 709, 714, 2251, 3335, 319, 321, 322, 323, 324, 386, 387, 2951, 418, 423, 424, 3009, 449, 450, 452, 2520}
            testSet = self.dataset.GetAntiTestSetForUserData(20000, user_items)
            
            predictions = algo.GetAlgorithm().test(testSet)
            
            recommendations = []
            
            print ("\nWe recommend:")
            for userID, movieID, actualRating, estimatedRating, _ in predictions:
                intMovieID = int(movieID)
                if(intMovieID in algo.dataset.movies):
                    recommendations.append((intMovieID, estimatedRating))
            
            recommendations.sort(key=lambda x: x[1], reverse=True)
            for ratings in recommendations[:10]:
                print(ml.getMovieName(ratings[0]), ratings[1])
                

            
            
    
    