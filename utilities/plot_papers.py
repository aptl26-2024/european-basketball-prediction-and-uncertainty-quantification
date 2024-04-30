import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

class plot_papers:
    
    
    def line_plot_tournament_per_model(self, evaluation_results, title, metric, loc=0):
        models = ['Logistic Regression', 'Random Forest', 'XGBoost', 'Ensemble Learning']
        tournaments = ['Greek Basket League', 'Liga ACB', 'Euroleague', 'Eurocup']
        colors = ['tab:blue','tab:red','tab:orange','tab:green']
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)


        for i in range(len(evaluation_results)):
            ax.plot(models,evaluation_results[i],label=tournaments[i],color=colors[i],linewidth=4,marker='o',markersize=12)



        ax.set_title(title, fontsize=30)
        ax.set_ylabel(metric, fontsize=18)
        ax.set_xlabel('Predictive Models', fontsize=18)
        ax.legend(loc=loc,prop={'size': 15})
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        ax.xaxis.set_tick_params(labelsize=18)
        ax.yaxis.set_tick_params(labelsize=18)
        
        return plt
    
    def line_plot_difference_baseline_full_information_model(self, differences, title, loc=0):
        
        metrics = ['Brier Score' , 'Accuracy' , 'F1-Score']
        tournaments = ["Greek Basket League","Liga ACB" ,"Euroleague","Eurocup"]
        colors = ['tab:red','tab:blue','tab:green']
        #colors = ['tab:purple','tab:cyan','tab:olive']

        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)



        for i in range(len(differences)):
            ax.plot(tournaments,differences[i],label=metrics[i],color=colors[i],linewidth=4,marker='o',markersize=12)



        ax.set_title(title, fontsize=30)
        ax.set_ylabel('Differences Of Values', fontsize=18)
        ax.set_xlabel('Tournaments', fontsize=18)
        ax.legend(loc=loc, prop={'size': 15})
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        ax.xaxis.set_tick_params(labelsize=18)
        
        return plt
    
    def barplot_comparison_train_set(self, full_greek_all, full_greek_same,full_spain_all,full_spain_same ,full_euroleague_all,
                                     full_euroleague_same,full_eurocup_all,full_eurocup_same, baseline_greek_all, baseline_greek_same,
                                     baseline_spain_all, baseline_spain_same, baseline_euroleague_all ,baseline_euroleague_same,
                                     baseline_eurocup_all, baseline_eurocup_same, title, metric, season,loc=0):
        
        full_greek_all_mean = np.mean(full_greek_all)
        full_greek_same_mean = np.mean(full_greek_same)
        full_spain_all_mean = np.mean(full_spain_all)
        full_spain_same_mean = np.mean(full_spain_same)
        full_euroleague_all_mean = np.mean(full_euroleague_all)
        full_euroleague_same_mean = np.mean(full_euroleague_same)
        full_eurocup_all_mean = np.mean(full_eurocup_all)
        full_eurocup_same_mean = np.mean(full_eurocup_same)


        baseline_greek_all_mean = np.mean(baseline_greek_all)
        baseline_greek_same_mean = np.mean(baseline_greek_same)
        baseline_spain_all_mean = np.mean(baseline_spain_all)
        baseline_spain_same_mean = np.mean(baseline_spain_same)
        baseline_euroleague_all_mean = np.mean(baseline_euroleague_all)
        baseline_euroleague_same_mean = np.mean(baseline_euroleague_same)
        baseline_eurocup_all_mean = np.mean(baseline_eurocup_all)
        baseline_eurocup_same_mean = np.mean(baseline_eurocup_same)
        
        
        full_greek_all_std = np.std(full_greek_all)
        full_greek_same_std = np.std(full_greek_same)
        full_spain_all_std = np.std(full_spain_all)
        full_spain_same_std = np.std(full_spain_same)
        full_euroleague_all_std = np.std(full_euroleague_all)
        full_euroleague_same_std = np.std(full_euroleague_same)
        full_eurocup_all_std = np.std(full_eurocup_all)
        full_eurocup_same_std = np.std(full_eurocup_same)


        baseline_greek_all_std = np.std(baseline_greek_all)
        baseline_greek_same_std = np.std(baseline_greek_same)
        baseline_spain_all_std = np.std(baseline_spain_all)
        baseline_spain_same_std = np.std(baseline_spain_same)
        baseline_euroleague_all_std = np.std(baseline_euroleague_all)
        baseline_euroleague_same_std = np.std(baseline_euroleague_same)
        baseline_eurocup_all_std = np.std(baseline_eurocup_all)
        baseline_eurocup_same_std = np.std(baseline_eurocup_same)
        
        
        
        full_all_train_mean = [full_greek_all_mean,full_spain_all_mean,full_euroleague_all_mean,full_eurocup_all_mean]
        
        full_same_year_train_mean = [full_greek_same_mean,full_spain_same_mean,full_euroleague_same_mean,full_eurocup_same_mean]

        baseline_all_train_mean = [baseline_greek_all_mean,baseline_spain_all_mean,baseline_euroleague_all_mean,
                                   baseline_eurocup_all_mean]
        
        baseline_same_year_train_mean = [baseline_greek_same_mean,baseline_spain_same_mean,baseline_euroleague_same_mean,
                                         baseline_eurocup_same_mean]
        
        full_all_train_std = [full_greek_all_std,full_spain_all_std,full_euroleague_all_std,full_eurocup_all_std]
        full_same_year_train_std = [full_greek_same_std,full_spain_same_std,full_euroleague_same_std,full_eurocup_same_std]

        baseline_all_train_std = [baseline_greek_all_std,baseline_spain_all_std,baseline_euroleague_all_std,baseline_eurocup_all_std]
        baseline_same_year_train_std =[baseline_greek_same_std,baseline_spain_same_std,baseline_euroleague_same_std,
                                       baseline_eurocup_same_std]
        
        n_groups = 4
        fig, ax = plt.subplots(figsize=(15,8))
        index = index = np.arange(n_groups)
        bar_width = 0.15
        opacity = 0.8

        rects1 = plt.bar(index, full_all_train_mean,yerr=full_all_train_std, width = bar_width,alpha=opacity,color='blue',
                 label='Full Information Model All years',ecolor='black',capsize=10)

        rects2 = plt.bar(index+bar_width, full_same_year_train_mean,yerr=full_same_year_train_std, width = bar_width,
                 alpha=opacity,color='royalblue',label='Full Information Model '+season,ecolor='black',capsize=10)


        rects3 = plt.bar(index+2*bar_width, baseline_all_train_mean,yerr=baseline_all_train_std, width = bar_width,
                 alpha=opacity,color='green',label='Baseline All years',ecolor='black',capsize=10)

        rects4 = plt.bar(index+3*bar_width, baseline_same_year_train_mean,yerr=baseline_same_year_train_std, 
                 width = bar_width,alpha=opacity,color='seagreen',label='Baseline '+season,ecolor='black',capsize=10)

        plt.xlabel('Tournament',fontsize=18)
        plt.ylabel(metric,fontsize=18)
        plt.title(title,fontsize=30)
        plt.xticks(index + bar_width*1.5, ("Greek Basket League","Liga ACB" ,"Euroleague","Eurocup"))
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.legend(loc=loc,prop={'size': 12})

        plt.tight_layout()
        
        return plt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        