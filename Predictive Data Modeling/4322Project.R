##########################
### Preparing the data ###
##########################
data = read.csv('/Users/alessandro/Downloads/pokemon_combined.csv')

# Load necessary libraries
if (!requireNamespace("corrplot", quietly = TRUE)) {
  install.packages("corrplot")
}
if (!requireNamespace("randomForest", quietly = TRUE)) {
  install.packages("randomForest")
}
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
if (!requireNamespace("tree", quietly = TRUE)) {
  install.packages("tree")
}
library(corrplot)
library(randomForest)
library(ggplot2)
library(tree)

##Check for null values, if any
null_values = is.na(data)
summary(null_values)

##no null values
unique(data)
summary(unique(data))

##Double-check: 2nd method
which(is.na(data))

unique(data$Growth.Rate)
##Encode the variables for Growth-Rate
##Slow = 1, Medium Slow = 2, Fluctuating = 3, Medium Fast = 4,
##Fast = 5, Erratic = 6

target_order =  c("Slow", "Medium Slow", "Fluctuating", "Medium Fast",
                  "Fast", "Erratic")
data$Growth.Rate = as.integer(factor(data$Growth.Rate, levels = target_order))

#Let's make a heat map to find out
numeric_data <- data[sapply(data, is.numeric)]
cor_matrix <- cor(numeric_data, use = "complete.obs")

##Create heat map
corrplot(cor_matrix, method = "circle", 
         type = "upper", order = "hclust", tl.cex = 0.8)

######################
### Decision Trees ###
######################
# Initialize arrays to store MSEs for each response variable
mse_speed <- numeric(10)
mse_attack <- numeric(10)
mse_defense <- numeric(10)
mse_hp <- numeric(10)

r_speed <- numeric(10)
r_attack <- numeric(10)
r_defense <- numeric(10)
r_hp <- numeric(10)

# Repeat the process 10 times
set.seed(1)  # Ensure reproducibility
for (i in 1:10) {
  # Randomly split data into 80% training and 20% testing
  train_indices <- sample(nrow(data), size = 0.8 * nrow(data))
  train_data <- data[train_indices, ]
  test_data <- data[-train_indices, ]
  
  # Train decision trees for each response variable
  speed_tree <- tree(Speed ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data)
  attack_tree <- tree(Attack ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data)
  defense_tree <- tree(Defense ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data)
  hp_tree <- tree(HP ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data)
  
  # Pruning for Speed Tree
  cv_speed <- cv.tree(speed_tree, FUN = prune.tree)  # Cross-validate
  best_size_speed <- cv_speed$size[which.min(cv_speed$dev)]
  pruned_speed <- prune.tree(speed_tree, best = best_size_speed)  # Prune tree
  
  # Pruning for Attack Tree
  cv_attack <- cv.tree(attack_tree, FUN = prune.tree)
  best_size_attack <- cv_attack$size[which.min(cv_attack$dev)]
  pruned_attack <- prune.tree(attack_tree, best = best_size_attack)
  
  # Pruning for Defense Tree
  cv_defense <- cv.tree(defense_tree, FUN = prune.tree)
  best_size_defense <- cv_defense$size[which.min(cv_defense$dev)]
  pruned_defense <- prune.tree(defense_tree, best = best_size_defense)
  
  # Pruning for HP Tree
  cv_hp <- cv.tree(hp_tree, FUN = prune.tree)
  best_size_hp <- cv_hp$size[which.min(cv_hp$dev)]
  pruned_hp <- prune.tree(hp_tree, best = best_size_hp)
  
  
  # Make predictions on the test data
  pred_speed <- predict(pruned_speed, test_data)
  pred_attack <- predict(pruned_attack, test_data)
  pred_defense <- predict(pruned_defense, test_data)
  pred_hp <- predict(pruned_hp, test_data)
  
  # Calculate and store MSEs
  mse_speed[i] <- mean((pred_speed - test_data$Speed)^2)
  mse_attack[i] <- mean((pred_attack - test_data$Attack)^2)
  mse_defense[i] <- mean((pred_defense - test_data$Defense)^2)
  mse_hp[i] <- mean((pred_hp - test_data$HP)^2)
  
  # Calculate R squared for each tree
  r_speed[i] <- cor(pred_speed, test_data$Speed)^2
  r_attack[i] <- cor(pred_attack, test_data$Attack)^2
  r_defense[i] <- cor(pred_defense, test_data$Defense)^2
  r_hp[i] <- cor(pred_hp, test_data$HP)^2
}
### Plot pruned examples ###
plot(pruned_speed)
text(pruned_speed, pretty = 0)

plot(pruned_attack)
text(pruned_attack, pretty = 0)

plot(pruned_defense)
text(pruned_defense, pretty = 0)

plot(pruned_hp)
text(pruned_hp, pretty = 0)

### Sum up for avg calculations ###
mean_mse_speed <- mean(mse_speed)
mean_mse_attack <- mean(mse_attack)
mean_mse_defense <- mean(mse_defense)
mean_mse_hp <- mean(mse_hp)

mean_r_speed <- mean(r_speed)
mean_r_attack <- mean(r_attack)
mean_r_defense <- mean(r_defense)
mean_r_hp <- mean(r_speed)

### Display Averages ###
cat(" Average RMSE for ten pruned Speed trees:", sqrt(mean_mse_speed), "\n", "Average RMSE for ten pruned Attack trees:", sqrt(mean_mse_attack), "\n", "Average RMSE for ten pruned Defense trees:", sqrt(mean_mse_defense), "\n", "Average RMSE for ten pruned HP trees:", sqrt(mean_mse_hp), "\n")
cat(" Average R^2 for ten pruned Speed trees:", mean_r_speed, "\n", "Average R^2 for ten pruned Attack trees:", mean_r_attack, "\n", "Average R^2 for ten pruned Defense trees:", mean_r_defense, "\n", "Average R^2 for ten pruned HP trees:", mean_r_hp, "\n")

######################
### Random Forests ###
######################
rfr_speed <- numeric(10)
rfr_attack <- numeric(10)
rfr_defense <- numeric(10)
rfr_hp <- numeric(10)

# Repeat the process 10 times
set.seed(1)  # Ensure reproducibility
for (i in 1:10) {
  # Randomly split data into 80% training and 20% testing
  train_indices <- sample(nrow(data), size = 0.8 * nrow(data))
  train_data <- data[train_indices, ]
  test_data <- data[-train_indices, ]
  
  # Random Forest for Speed
  rf_speed <- randomForest(Speed ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data, importance = TRUE, ntree = 500)
  pred_speed <- predict(rf_speed, newdata = test_data)
  mse_speed[i] <- mean((test_data$Speed - pred_speed)^2)
  rfr_speed[i] <- cor(pred_speed, test_data$Speed)^2
  
  # Random Forest for Attack
  rf_attack <- randomForest(Attack ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data, importance = TRUE, ntree = 500)
  pred_attack <- predict(rf_attack, newdata = test_data)
  mse_attack[i] <- mean((test_data$Attack - pred_attack)^2)
  rfr_attack[i] <- cor(pred_attack, test_data$Attack)^2
  
  # Random Forest for Defense
  rf_defense <- randomForest(Defense ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data, importance = TRUE, ntree = 500)
  pred_defense <- predict(rf_defense, newdata = test_data)
  mse_defense[i] <- mean((test_data$Defense - pred_defense)^2)
  rfr_defense[i] <- cor(pred_defense, test_data$Defense)^2
  
  # Random Forest for HP
  rf_hp <- randomForest(HP ~ Height + Weight + Catch.rate + Base.Exp. + Growth.Rate + Sp..Atk + Sp..Def, data = train_data, importance = TRUE, ntree = 500)
  pred_hp <- predict(rf_hp, newdata = test_data)
  mse_hp[i] <- mean((test_data$HP - pred_hp)^2)
  rfr_hp[i] <- cor(pred_hp, test_data$HP)^2
}

# Four Examples of Importance Plots
speed_plot <- varImpPlot(rf_speed, main = paste("Feature Importance for", "Speed"))
attack_plot <- varImpPlot(rf_attack, main = paste("Feature Importance for", "Attack"))
defense_plot <- varImpPlot(rf_defense, main = paste("Feature Importance for", "Defense"))
hp_plot <- varImpPlot(rf_hp, main = paste("Feature Importance for", "HP"))

# Calculate average MSEs across all 10 iterations
mean_mse_speed <- mean(mse_speed)
mean_mse_attack <- mean(mse_attack)
mean_mse_defense <- mean(mse_defense)
mean_mse_hp <- mean(mse_hp)

mean_r_speed <- mean(rfr_speed)
mean_r_attack <- mean(rfr_attack)
mean_r_defense <- mean(rfr_defense)
mean_r_hp <- mean(rfr_hp)
  
# Print the results
cat(" Average RMSE for ten Speed random forests:", sqrt(mean_mse_speed), "\n", "Average RMSE for ten Attack random forests:", sqrt(mean_mse_attack), "\n", "Average RMSE for ten Defense random forests:", sqrt(mean_mse_defense), "\n", "Average RMSE for ten HP random forests:", sqrt(mean_mse_hp), "\n")
cat(" Average R^2 for ten Speed random forests:", mean_r_speed, "\n", "Average R^2 for ten Attack random forests:", mean_r_attack, "\n", "Average R^2 for ten Defense random forests:", mean_r_defense, "\n", "Average R^2 for ten HP random forests:", mean_r_hp, "\n")

